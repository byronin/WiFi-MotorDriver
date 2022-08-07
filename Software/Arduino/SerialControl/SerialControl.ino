#define A1 14
#define A2 12
#define B1 15
#define B2 13
#define C1 2
#define C2 0
#define D1 5
#define D2 4
String Message;
void setup() {
  Serial.begin(115200);

  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(B1, OUTPUT);
  pinMode(B2, OUTPUT);
  pinMode(C1, OUTPUT);
  pinMode(C2, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(16, OUTPUT);

}

void loop() {
  if (Serial.available() > 0) {        // Save message from serial
    Message =  Serial.readString();
  }
  dc_drive(Message);
}


void dc_drive(String dc_cmd) {
  String dc_direction ;
  String str_speed  ;
  int dc_speed = 0 ;

  if (dc_cmd != "STOP\n") {
    int index1 = dc_cmd.indexOf(':');
    int index2 = dc_cmd.indexOf("\n");

    dc_direction =  dc_cmd.substring(0, index1);
    str_speed = dc_cmd.substring(index1 + 1, index2);
    Serial.println(dc_direction);
    Serial.println(str_speed);
    dc_speed = str_speed.toInt();
    digitalWrite(16, HIGH);
    dc_speed = map(dc_speed, 0, 100, 0, 255);
    if (dc_direction == "F") {
      analogWrite(A1, 0);
      analogWrite(A2, dc_speed);
      analogWrite(B1, 0);
      analogWrite(B2, dc_speed);
      analogWrite(C1, dc_speed);
      analogWrite(C2, 0);
      analogWrite(D1, dc_speed);
      analogWrite(D2, 0);
    } else if (dc_direction == "B") {
      analogWrite(A1, dc_speed);
      analogWrite(A2, 0);
      analogWrite(B1, dc_speed);
      analogWrite(B2, 0);
      analogWrite(C1, 0);
      analogWrite(C2, dc_speed);
      analogWrite(D1, 0);
      analogWrite(D2, dc_speed);
    } else if (dc_direction == "L") {
      analogWrite(A1, dc_speed);
      analogWrite(A2, 0);
      analogWrite(B1, dc_speed);
      analogWrite(B2, 0);
      analogWrite(C1, dc_speed);
      analogWrite(C2, 0);
      analogWrite(D1, dc_speed);
      analogWrite(D2, 0);
    } else if (dc_direction == "R") {
      analogWrite(A1, 0);
      analogWrite(A2, dc_speed);
      analogWrite(B1, 0);
      analogWrite(B2, dc_speed);
      analogWrite(C1, 0);
      analogWrite(C2, dc_speed);
      analogWrite(D1, 0);
      analogWrite(D2, dc_speed);
    }

  } else {
    digitalWrite(16, LOW);
    analogWrite(A1, 0);
    analogWrite(A2, 0);
    analogWrite(B1, 0);
    analogWrite(B2, 0);
    analogWrite(C1, 0);
    analogWrite(C2, 0);
    analogWrite(D1, 0);
    analogWrite(D2, 0);
  }
}
