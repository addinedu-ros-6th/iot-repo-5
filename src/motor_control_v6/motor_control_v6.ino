/*
 * TODO:
 * - Test byte data communication. 
 * - Add general data types. 
 *   -> position_x, position_y, direction_x, direction_y, currentMillis ... etc 
 *   -> position_x, position_y : int, direction_x, direction_y : bool, currentMillis, previousMillis : long 
 *   -> send_data = { deviceStatus, position_x, position_y, direction_x, direction_y, currentMillis, motorStatus, flameStatus, waterStatus }
 *   -> size = { 1, 2, 2, 1, 1, 4, 1, 1, 1 }, total_size = 15 bytes
 * - 
 */
#include <Servo.h>
#include <SPI.h>

// Pin settings
const int water_pin = A0;
const int relay_pin = 3;  // relay is for water pump
const int flame_pin = 4;  // maybe need analog pin. need experiment. If we want to assess the level of fire, analog pin is probably needed.
const int buzzer_pin = 5;  // passive buzzer is the one without sticker 

// Motor settings
int position_x = 0;
int position_y = 0;
bool direction_x = true;  // true: positive direction
bool direction_y = true;  // false: negative direction
Servo servo_x;
Servo servo_y;

byte converted_pos_x[2];
byte converted_pos_y[2];
byte converted_dir_x;
byte converted_dir_y;

// Buzzer settings
long currentMillis = 0;
long previousMillis = 0;
bool toneFlag = true;  // if true, emit G note. if false, emit D note.

byte converted_currMillis[4];

// Sensor data
byte deviceStatus = 0x00;
byte motorStatus = 0x00;
byte flameStatus = 0x00;  // 0x00: nothing detected.
byte waterStatus = 0x00;  // 0x01: something happened.

const int recv_buffer_size = 16;  // 사실 16까지는 필요없을거임. 나중에 조정하셈. 
const int send_buffer_size = 16;  // 여기는 16까지 필요함. 
byte send_buffer[send_buffer_size];

int count = 0;


void setup()
{
  Serial.begin(9600);
  servo_x.attach(8);
  servo_y.attach(9);

  pinMode(relay_pin, OUTPUT);
  pinMode(flame_pin, INPUT);

  memset(send_buffer, 0x00, send_buffer_size);
}

void loop()
{
  deviceStatus = 0x01;
  motorStatus = 0x00;
  waterStatus = 0x00;
  flameStatus = 0x00;

  int recv_size = 0;
  char recv_buffer[recv_buffer_size];
  memset(recv_buffer, 0x00, recv_buffer_size);

  if (Serial.available() > 0)
  {
    recv_size = Serial.readBytesUntil('\n', recv_buffer, recv_buffer_size);
  }

  if (recv_size > 0)
  {
    String recv_data = String((char*)recv_buffer);  // 바이트 데이터를 문자열로 바꾸기

    int pair_count = recv_data.length() / 2;  // 문자열 쌍 개수 저장
    String pairs[pair_count];  // 문자열 쌍 만큼 배열 크기 지정

    for (int i = 0; i < pair_count; i++)
    {
      pairs[i] = recv_data.substring(i*2, i*2+2);
    }

    // 여기부터 명령 처리 부분 시작. 
    for (int i = 0; i < pair_count; i++)
    {
      switch (pairs[i].charAt(0))
      {
        // patrol mode
        case '0':
          noTone(buzzer_pin);
          digitalWrite(relay_pin, LOW);
          // Serial.print("Patrol mode entered! ");
          patrol_mode(motorStatus, direction_x, direction_y, position_x, position_y);
          break;
        
        // aiming mode
        case '1':
          noTone(buzzer_pin);
          digitalWrite(relay_pin, LOW);
          // Serial.print("Aiming mode entered! ");
          aiming_mode(motorStatus, pairs[i].charAt(1), count, position_x, position_y);
          break;
        
        // flame detecting mode
        case '2':
          digitalWrite(relay_pin, LOW);
          Serial.print("Flame detecting mode entered!! ");
          if (digitalRead(flame_pin) < 800)  // 나중에 조정하기
          {
            // Put flame on signal here
            flameStatus = 0x01;
          }
          else
          {
            // Put flame off signal here
            flameStatus = 0x00;
          }
          break;
        
        // firing mode
        case '3':
          noTone(buzzer_pin);

          // Turn on the pump
          digitalWrite(relay_pin, HIGH);

          // Turn on the buzzer
          if (currentMillis - previousMillis > 500)
          {
            previousMillis = currentMillis;
            toneFlag = !toneFlag;
          }

          if (toneFlag)
          {
            tone(buzzer_pin, 784);
          }
          else
          {
            tone(buzzer_pin, 587);
          }
          break;
        
        // manual mode
        case '4':
          noTone(buzzer_pin);
          digitalWrite(relay_pin, LOW);
          Serial.print("Manual mode entered! ");

          switch (pairs[i].charAt(1))
          {
            case '0':
              break;
            
            case '1':
              digitalWrite(relay_pin, HIGH);
              break;
            
            case '2':
              digitalWrite(relay_pin, LOW);
              break;
          }
          break;
        
        case '5':
          break;
      }
    }

    // Send received commands
    // for (int i = 0; i < pair_count; i++)
    // {
    //   Serial.print(pairs[i]);
    //   Serial.print(' ');
    // }

    // 여기에 두면 불 없을때 렉걸린다. 불 없을때라기보다는 받는 명령이 없을때 렉걸린다. 항상 어떤 명령을 받도록 파이썬을 짜라. 
    Serial.print(' ');
    Serial.println();
  }

  // Serial.print(' ');
  // Serial.println();

  servo_x.write(position_x);
  servo_y.write(position_y);

  // water level detection
  if (analogRead(water_pin) < 650)
  {
    // Put water level low signal here
    waterStatus = 0x01;
  }
  else
  {
    waterStatus = 0x00;
  }

  // Send sensor data
  // Serial.write(deviceStatus);
  // Serial.write(motorStatus);
  // Serial.write(flameStatus);
  // Serial.write(waterStatus);
  // Serial.println();  // Send data to PC via serial communication

  count++;
}



// Convert int data type to byte data type.
void intToByte( byte* buffer, int data )
{
  buffer[0] = data & 0xFF;
  buffer[1] = (data >> 8) & 0xFF;
}

// Convert bool data type to byte data type.
byte boolToByte( bool data )
{
  byte converted = (byte)data;

  return converted;
}

// Convert long data type to byte data type.
void longToByte( byte* buffer, long data )
{
  buffer[0] = data & 0xFF;
  buffer[1] = (data >> 8) & 0xFF;
  buffer[2] = (data >> 16) & 0xFF;
  buffer[3] = (data >> 24) & 0xFF;
}


/*
 * Patrol between designated coordinates. 
 * x-range: 45-135
 * y-range: 60-90
 */
void patrol_mode(byte& motorStatus, bool& direction_x, bool& direction_y, int& position_x, int& position_y)
{
  motorStatus = 0x01;

  if (position_x <= 45)
  {
    direction_x = true;
  }
  else if (position_x >= 135)
  {
    direction_x = false;
  }

  if (position_y <= 60)
  {
    direction_y = true;
  }
  else if (position_y >= 90)
  {
    direction_y = false;
  }

  if (direction_x)
  {
    position_x++;
  }
  else
  {
    position_x--;
  }

  if (direction_y)
  {
    position_y++;
  }
  else
  {
    position_y--;
  }

  // Serial.print(position_x);
  // Serial.print(' ');
  // Serial.print(position_y);
  // Serial.print(' ');
}

// Aim the nozzle at the fire 
void aiming_mode(byte& motorStatus, char cmd, int count, int& position_x, int& position_y)
{
  motorStatus = 0x01;

  switch (cmd)
  {
    case '0':
      Serial.print("No fire detected ");
      break;

    case '1':
      Serial.print("x-- entered ");
      position_x--;
      break;
    
    case '2':
      Serial.print("x++ entered ");
      position_x++;
      break;
    
    case '3':
      Serial.print("y-- entered ");
      position_y++;
      break;

    case '4':
      Serial.print("y++ entered ");
      position_y--;
      break;
    
    case '5':
      if (count % 3 == 0)
      {
        Serial.print("slow x-- entered ");
        position_x--;
      }
      break;
    
    case '6':
      if (count % 3 == 0)
      {
        Serial.print("slow x++ entered ");
        position_x++;
      }
      break;
    
    case '7':
      if (count % 3 == 0)
      {
        Serial.print("slow y-- entered ");
        position_y++;
      }
      break;
    
    case '8':
      if (count % 3 == 0)
      {
        Serial.print("slow y++ entered ");
        position_y--;
      }
      break;
    
    default:
      break;
  }
}



























