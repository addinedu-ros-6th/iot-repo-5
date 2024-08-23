/*
 * TODO:
 * - Test byte data communication. 
 * - Add general data types. 
 *   -> position_x, position_y, direction_x, direction_y, currentMillis ... etc 
 *   -> position_x, position_y : int, direction_x, direction_y : bool, currentMillis, previousMillis : long 
 *   -> send_data = { deviceStatus, currentMillis, position_x, position_y, direction_x, direction_y, motorStatus, flameStatus, waterStatus }
 *   -> size = { 1, 4, 1, 1, 1, 1, 1, 1, 1 }, total_size = 12 bytes
 * - 
 */
#include <Servo.h>
#include <SPI.h>

// Pin settings
const int flame_pin = A0;
const int water_pin = 3;
const int relay_pin = 4;
const int buzzer_pin = 5;


// Motor settings
int position_x = 0;
int position_y = 0;
bool direction_x = true;  // true: positive direction
bool direction_y = true;  // false: negative direction
Servo servo_x;
Servo servo_y;

byte converted_pos_x;
byte converted_pos_y;
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
bool send_signal;


void setup()
{
  Serial.begin(9600);
  servo_x.attach(8);
  servo_y.attach(9);

  pinMode(relay_pin, OUTPUT);
  pinMode(flame_pin, INPUT);

  memset(send_buffer, 0x00, send_buffer_size);
  memset(converted_currMillis, 0x00, 4);

  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  send_signal = false;
  currentMillis = millis();

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
          patrol_mode(motorStatus, direction_x, direction_y, position_x, position_y);
          break;
        
        // aiming mode
        case '1':
          noTone(buzzer_pin);
          digitalWrite(relay_pin, LOW);
          aiming_mode(motorStatus, pairs[i].charAt(1), count, position_x, position_y);
          break;
        
        // flame detecting mode
        case '2':
          noTone(buzzer_pin);
          digitalWrite(relay_pin, LOW);
          break;
        
        // firing mode
        case '3':
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
        
        case '9':
          send_signal = true;
          break;
      }
    }
  }

  servo_x.write(position_x);
  servo_y.write(position_y);

  // water level detection
  // 1 when water. 0 when no water.
  if (digitalRead(water_pin))
  {
    waterStatus = 0x00;
  }
  else
  {
    waterStatus = 0x01;
  }

  if (analogRead(flame_pin) < 800)  // 나중에 조정하기
  {
    flameStatus = 0x01;
    // digitalWrite(LED_BUILTIN, HIGH);
  }
  else
  {
    flameStatus = 0x00;
    // digitalWrite(LED_BUILTIN, LOW);
  }

  // Send sensor data
  converted_pos_x = intToByte(position_x);
  converted_pos_y = intToByte(position_y);
  converted_dir_x = boolToByte(direction_x);
  converted_dir_y = boolToByte(direction_y);
  longToByte(converted_currMillis, currentMillis);

  memcpy(send_buffer, &deviceStatus, 1);
  memcpy(send_buffer+1, converted_currMillis, 4);
  memcpy(send_buffer+5, &converted_pos_x, 1);
  memcpy(send_buffer+6, &converted_pos_y, 1);
  memcpy(send_buffer+7, &converted_dir_x, 1);
  memcpy(send_buffer+8, &converted_dir_y, 1);
  memcpy(send_buffer+9, &motorStatus, 1);
  memcpy(send_buffer+10, &flameStatus, 1);
  memcpy(send_buffer+11, &waterStatus, 1);

  if (send_buffer[10] == 0x01)
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else 
  {
    digitalWrite(LED_BUILTIN, LOW);
  }

  if (send_signal)
  {
    // for (int i = 0; i < 12; i++)
    // {
    //   Serial.print(send_buffer[i]);
    //   Serial.print("//");
    // }
    Serial.write(send_buffer, 12);
    Serial.println();
  }

  count++;
}



// Convert int data type to byte data type.
byte intToByte( int data )
{
  byte converted = (byte)data;

  return converted;
}
// void intToByte( byte* buffer, int data )
// {
//   buffer[0] = data & 0xFF;
//   buffer[1] = (data >> 8) & 0xFF;
// }

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

  if (position_y <= 90)
  {
    direction_y = true;
  }
  else if (position_y >= 120)
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
}

// Aim the nozzle at the fire 
void aiming_mode(byte& motorStatus, char cmd, int count, int& position_x, int& position_y)
{
  motorStatus = 0x01;

  switch (cmd)
  {
    case '0':
      break;

    case '1':
      position_x--;
      break;
    
    case '2':
      position_x++;
      break;
    
    case '3':
      position_y++;
      break;

    case '4':
      position_y--;
      break;
    
    case '5':
      if (count % 3 == 0)
      {
        position_x--;
      }
      break;
    
    case '6':
      if (count % 3 == 0)
      {
        position_x++;
      }
      break;
    
    case '7':
      if (count % 3 == 0)
      {
        position_y++;
      }
      break;
    
    case '8':
      if (count % 3 == 0)
      {
        position_y--;
      }
      break;
    
    default:
      break;
  }
}



























