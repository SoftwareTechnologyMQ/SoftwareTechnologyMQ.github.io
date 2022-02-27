import processing.svg.*;
PrintWriter writer;
int counter = 1;
final int GAP = 4;
final int LENGTH = 4;
boolean paused = false;
final int N = 10;

void setup() {
  size(400, 400);
  background(255);
  frameRate(30);
}

boolean anySame(int[] data) {
  for (int i=0; i < data.length; i++) {
    for (int k=i+1; k < data.length; k++) {
      if (data[i] == data[k]) {
        return true;
      }
    }
  }
  return false;
}

void draw() {
  if (!paused) {
    String suffix = (int)random(Integer.MAX_VALUE)+""+(int)random(Integer.MAX_VALUE);
    // Note that #### will be replaced with the frame number. Fancy!
    beginRecord(SVG, "log"+suffix+"/frame"+suffix+".svg");
    writer = createWriter("log"+suffix+"/toBeFilled"+suffix+".txt");
    background(255);
    grid();
    noFill();
    stroke(2);
    rect(1, 1, width-3, height-3);
    int[] pos = new int[4];

    while (anySame(new int[]{pos[0], pos[1], pos[2], pos[3]})) {
      int mult = (int)width/N;
      pos[0] = mult*(int)random(1, 3);
      pos[1] = mult*(int)random(4, 8);
      pos[2] = mult*(int)random(4, 8);
      pos[3] = mult*(int)random(1, 3);

      if (random(1) < 0.5) {
        pos[0] = mult*(int)random(1, 3);
        pos[1] = mult*(int)random(1, 3);
        pos[2] = mult*(int)random(4, 8);
        pos[3] = mult*(int)random(4, 8);
      }
    }

    strokeWeight(1);
    if(pos[0] < 200) {
      if(pos[1] < 200){
        dash(pos[0], pos[1]);
      }else {
        dash(pos[0], pos[1]+pos[2]);
      }
    }else{
      if(pos[1] < 200){
        dash(pos[0] + pos[2], pos[1]);
       }else {
        dash(pos[0] + pos[2], pos[1] + pos[2]);
      }
    }

    strokeWeight(4);
    stroke(255, 0, 0);
    noFill();
    rect(pos[0], pos[1], pos[2], pos[3]);
    stroke(0);

    writer.write("rect\n");
    writer.write(pos[0]+"\n");
    writer.write(pos[1]+"\n");
    writer.write(pos[2]+"\n");
    writer.write(pos[3]+"");
    writer.flush();
    writer.close();
    save("log"+suffix+"/output"+suffix+".png");
    counter++;
    endRecord();
    if (counter>=50) {
      exit();
    }
  }
}

void mousePressed() {
  paused = !paused;
}

void grid() {
  strokeWeight(1);
  stroke(200);
  for (int i=0; i<width; i+=width/N) {
    line(i, 0, i, height);
  }
  for (int i=0; i<height; i+=height/N) {
    line(0, i, width, i);
  }
}

void dash(float x1, float y1, float x2, float y2, String purpose) {
  if (x1 == x2) {
    for (float y=min(y1, y2); y<max(y1, y2); y+=(GAP+LENGTH)) {
      line(x1, y, x1, y+LENGTH);
    }
    fill(0);
    textAlign(CENTER, CENTER);
    text(purpose+" = "+(int)abs(y1-y2), x1, (y1+y2)/2);
  } else {
    if (x1 > x2) {
      float temp = x1;
      x1 = x2;
      x2 = temp;

      temp = y1;
      y1 = y2;
      y2 = temp;
    }

    strokeWeight(1);
    float gradient = (y2-y1)/(x2-x1);
    for (float x=x1, y=y1; x<x2; x+=(GAP+LENGTH), y=y+(GAP+LENGTH)*gradient) {
      line(x, y, x+2, y+(GAP+LENGTH)/2*gradient);
    }

    fill(0);
    textAlign(CENTER, CENTER);
    text(purpose+" = "+(int)dist(x1, y1, x2, y2), (x1+x2)/2, (y1+y2)/2);
  }
}

//vertical and horizontal dashes from point (x, y)
void dash(float x, float y) { 
  vdash(x, y);
  hdash(x, y);
}

void vdash(float x, float y) {
  textAlign(LEFT, CENTER);
  fill(0);
  if (y < height/2) {
    for (float i=0; i<y; i+=(GAP+LENGTH)) {
      line(x, i, x, i+LENGTH);
    }
    text((int)y+"", x, y/2);
  } else {
    for (float i=y; i<height; i+=(GAP+LENGTH)) {
      line(x, i, x, i+LENGTH);
    }
    text((int)(height-y)+"", x, y + (height - y)/2);
  }
}

void hdash(float x, float y) {
  textAlign(CENTER, TOP);
  fill(0);
  if (x < width/2) {
    for (float i=0; i<x; i+=(GAP+LENGTH)) {
      line(i, y, i+LENGTH, y);
    }
    text((int)x+"", x/2, y);
  } else {
    for (float i=x; i<width; i+=(GAP+LENGTH)) {
      line(i, y, i+LENGTH, y);
    }
    text((int)(width-x)+"", x + (width - x)/2, y);
  }
}
