/*
*reference co2 levels:
*atmospheric level 400ppm
*avg indoor level 350-450 ppm
*maxium acceptable ppm 1000ppm
*dangerous level 2000ppm 
*/



#define aninput A3

void setup()
{
    pinMode(aninput,INPUT);
    while (!Serial);
    Serial.begin(9600);
    
    }


void loop()
 { 
      int co2now[10];   /*setting up variables for the data.*/ 
      int co2raw = 0;   /*c02 reading var, raw c02 value var, calculated ppm var*, average var*/
      int co2ppm = 0;
      int zzz = 0;                      
                            
for (int x = 0;x<10;x++) /*takes sample reading of c02 once for 2 seconds*/         
{
  co2now[x] = analogRead(A3);
  delay(1000);
  }             
                            
for (int x = 0;x<10;x++) /*adds all readings together before dividing to get mean*/         
{
 zzz=zzz + co2now[x];
  }              
/*divides samples by 10 to get mean, and final calculated ppm*/                                 
co2raw = zzz/10;         
co2ppm = co2raw;                         
          
/*print out values*/
Serial.print("Air Quality: ");
Serial.print(co2ppm);
Serial.println("PPM");


}
     
