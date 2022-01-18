float gap = 100; //<>// //<>//
float period = 3000;
float startAt = 500;
color darkest = color(247, 123, 0);
long pmillis;

color[] colours = {color(247, 146, 2), color(247, 161, 2), color(247, 133, 5), darkest};

void setup() {
  size(1280, 720);
  noStroke();
  textFont(loadFont("HiraMaruPro-W4-60.vlw"), 60);
}

void draw() {
  background(darkest);
  pmillis = millis() % 16000;
  for (int round = 0; round < 4; round++) {
    float leaderX = max(0, pmillis-(startAt+period*round));
    for (int i = 0; i < 5; i++) {
      float linear = (max(0, leaderX - i*gap)/width);
      float animated = (1 - pow(2, -2*linear))*1.5*width; // FIXME
      fill(colours[round]);
      if (round % 2 == 0) {
        rect(0, i*(height/5), animated, height/5);
      } else {
        rect(width-animated, i*(height/5), animated, height/5);
      }
    }
  }
  fill(255);
  text("software technology", 630, 650);
}
