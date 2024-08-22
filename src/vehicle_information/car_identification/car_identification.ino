#include <SPI.h>

// Pin settings
const int VEHICLE_TYPE_LED = 8;
const int IS_ELEC_LED = 9;
const int PLATE_NUM_LED = 10;


const int BUFFER_SIZE = 4; 

void setup() {
  Serial.begin(9600);
  pinMode(VEHICLE_TYPE_LED, OUTPUT);
  pinMode(IS_ELEC_LED, OUTPUT);
  pinMode(PLATE_NUM_LED, OUTPUT);
}

void loop() {

  int recv_size = 0;
  char recv_buffer[BUFFER_SIZE];
  memset(recv_buffer, 0x00, BUFFER_SIZE);

  if (Serial.available() > 0) 
  {
    recv_size = Serial.readBytesUntil('\n', recv_buffer, BUFFER_SIZE);
  }

  if (recv_size > 0)
  {
    String recv_data = String((char*)recv_buffer);

    if (recv_data[0] == '1')
    {
      digitalWrite(VEHICLE_TYPE_LED, HIGH);
    }
    else
    {
      digitalWrite(VEHICLE_TYPE_LED, LOW);
    }
    
    if (recv_data[1] == '1')
    {
      digitalWrite(IS_ELEC_LED, HIGH);
    }
    else
    {
      digitalWrite(IS_ELEC_LED, LOW);
    }

    if (recv_data[2] == '1')
    {
      digitalWrite(PLATE_NUM_LED, HIGH);
    }
    else
    {
      digitalWrite(PLATE_NUM_LED, LOW);
    }
  }

}
