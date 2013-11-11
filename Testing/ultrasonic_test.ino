/**
 * Test code for testing the analog output of 
 * the XL-MaxSonar EZ/AE ultrasonic range finder
 * 
 * Author: Thai Nguyen
 * Date: November 11, 2013
 */

#define BAUD_RATE 9600 // UART baud rate
#define VCC		  5.0  // Supply voltage to ultrasonic range finder
#define ADC_RES   1023 // ADC resolution

int sensorPin = A0;
int distance;

double adc2Distance(int adcvalue) {
	return adcvalue * VCC / ADC_RES;
}

void setup() {
	//Setup serial
	Serial.begin(BAUD_RATE, SERIAL_8N1);
}

void loop() {
	// read the value from the sensor
	sensorValue = analogRead(sensorPin);
	// convert adc level to a distance
	distance = adc2Distance(sensorValue);
	// output value to computer
	Serial.write(distance);
	Serial.write("\n");
}