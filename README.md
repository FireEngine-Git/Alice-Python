I Didnt Put The Data Folder Bcz It Consisted Of The API Key But You Can Create a Data Folder and Create A Text File Called "API.txt" and Put You Key And The Rest Will Be Handled By The Code Also You Might Need To Change The Com Port In Python Part
And
I Couldnt Upload The Arduino Part So Heres The Code For It

```cpp
#include <Adafruit_SSD1306.h>
#include <FluxGarage_RoboEyes.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

RoboEyes<Adafruit_SSD1306> roboEyes(display); 
bool firstMood = true;

void Laughing(int time){
  roboEyes.setMood(HAPPY);
  roboEyes.setVFlicker(true, 4);
  unsigned long startTime = millis(); 
  while (millis() - startTime < time*1000) {
    roboEyes.update(); // This keeps the animation moving during the "wait"
  }
  roboEyes.setVFlicker(0, 0);
  roboEyes.setMood(DEFAULT);
  roboEyes.update();
}

void Confused(int time){
  roboEyes.setHFlicker(1, 10);
  unsigned long startTime = millis(); 
  while (millis() - startTime < time*1000) {
    roboEyes.update(); // This keeps the animation moving during the "wait"
  }
  roboEyes.setHFlicker(0, 0);
  roboEyes.setMood(DEFAULT);
  roboEyes.update();
}

void Idle(bool idle){
    roboEyes.setMood(DEFAULT);
    roboEyes.update();
    roboEyes.setAutoblinker(idle, 2, 1);
    roboEyes.setIdleMode(idle, 2, 1);
    roboEyes.update();
}

void setup() {
  Serial.begin(9600);
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  roboEyes.begin(SCREEN_WIDTH, SCREEN_HEIGHT, 100);
  roboEyes.close();
}

void loop() {
  roboEyes.update();
  if (Serial.available()){
    int mood = Serial.readString().toInt();
    Serial.println(mood);
    roboEyes.setPosition(123);
    roboEyes.open();
    Idle(false);
    if (mood <= 3){
      roboEyes.setMood(mood);

      if (!firstMood) {
        unsigned long startTime = millis(); 
        while (millis() - startTime < 2000) {
          roboEyes.update();
        }
  
        Idle(true);
      }   
      else {
        roboEyes.update();
      }
    }
    else {
      int time = 4;
      if (!firstMood){
        time = 2;
      }
      switch (mood) {
        case 4:
          Laughing(time);
          Idle(true);
          break;
        case 5:
          Confused(time);
          Idle(true);
          break;
        case 6:
          roboEyes.close();
          break;
      }
    }
    firstMood = !firstMood;

  }
}
