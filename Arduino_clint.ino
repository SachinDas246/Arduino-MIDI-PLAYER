int brt1 = 9000, pst1 = 291, len1 = 13381, ECln1 = 483; ////brk time is in micro // pst1 is in milli
//int brt2 = 134, pst2 = 111, len2 = 100;

String p = "";

//Change pin , if required
const int note1 = 2; // first note pin
const int note2 = 3;
const int note3 = 4;
const int note4 = 5;
const int note5 = 6;
const int note6 = 7;
const int note7 = 8; // Last note pin

void setup()
{

  pinMode(note1, OUTPUT);
  pinMode(note2, OUTPUT);
  pinMode(note3, OUTPUT);
  pinMode(note4, OUTPUT);
  pinMode(note5, OUTPUT);
  pinMode(note6, OUTPUT);
  pinMode(note7, OUTPUT);

  pinMode(13, OUTPUT);
  Serial.begin(9600);

////Wait for starting///////
bak1:
  while (!Serial.available())
  {
  }
  String s = Serial.readString();
  if (s != "start")
  {
    Serial.println(s);
    goto bak1;
  }
  else
  {
    Serial.println("o");
  }

  ///////// 1st Song PLayer ////////
  while (!Serial.available())
  {
  }
  p = Serial.readString();

  String p = "a2";
  int i = 0;
  int m = 0;
  while (1)
  {
    playSet(p.substring(i, i + 7)); //turn on the switch according to the pattern
    if ((i + 7 == ECln1) && (m + 7 != len1))
    {
      Serial.println("o");
    }                               // request for next block of codes
    delay(pst1);                    // Past delay
    breaker(p.substring(i, i + 7)); // check if there are any brakes if so apply
    delayMicroseconds(brt1);        // Break delay
    m = m + 7;
    if (m == len1)
    {
      Serial.println("k"); // End
      break;
    }
    i = i + 7;
    if (i == ECln1)
    {
      digitalWrite(13, 1);
      while (!Serial.available()) // wait for next data
      {
      }
      p = Serial.readString(); // read next data

      i = 0;
      digitalWrite(13, 0);
    }
  }
}

void playSet(String cod) // function to r
{
  // set pin 2
  if (cod.charAt(0) == '0')
  {
    digitalWrite(note1, 0);
    noTone(9);
  }
  else
  {
    digitalWrite(note1, 1);
    tone(9, 500);
  }

  // set pin 3
  if (cod.charAt(1) == '0')
  {
    digitalWrite(note2, 0);
  }
  else
  {
    digitalWrite(note2, 1);
  }

  // set pin 4
  if (cod.charAt(2) == '0')
  {
    digitalWrite(note3, 0);
  }
  else
  {
    digitalWrite(note3, 1);
  }

  // set pin 5
  if (cod.charAt(3) == '0')
  {
    digitalWrite(note4, 0);
  }
  else
  {
    digitalWrite(note4, 1);
  }

  // set pin 6
  if (cod.charAt(4) == '0')
  {
    digitalWrite(note5, 0);
  }
  else
  {
    digitalWrite(note5, 1);
  }

  // set pin 7
  if (cod.charAt(5) == '0')
  {
    digitalWrite(note6, 0);
  }
  else
  {
    digitalWrite(note6, 1);
  }

  // set pin 8
  if (cod.charAt(6) == '0')
  {
    digitalWrite(note7, 0);
  }
  else
  {
    digitalWrite(note7, 1);
  }
}

void breaker(String cod)
{

  // set pin 2
  if (cod.charAt(0) == 'b')
  {
    digitalWrite(note1, 0);
    //noTone(9);
    //digitalWrite(13, 1);
  }

  // set pin 3
  if (cod.charAt(1) == 'b')
  {
    digitalWrite(note2, 0);
  }

  // set pin 4
  if (cod.charAt(2) == 'b')
  {
    digitalWrite(note3, 0);
  }

  // set pin 5
  if (cod.charAt(3) == 'b')
  {
    digitalWrite(note4, 0);
  }

  // set pin 6
  if (cod.charAt(4) == 'b')
  {
    digitalWrite(note5, 0);
  }

  // set pin 7
  if (cod.charAt(5) == 'b')
  {
    digitalWrite(note6, 0);
  }

  // set pin 8
  if (cod.charAt(6) == 'b')
  {
    digitalWrite(note7, 0);
  }
}

void loop() {}
