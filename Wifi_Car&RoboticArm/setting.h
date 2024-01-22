#include <ESP8266WiFi.h>

//配置 静态 IP

IPAddress staticIP(192, 168, 1, 99); //esp8266 开发板的IP地址

IPAddress gateway(192, 168, 1, 1); //网关  路由器的IP地址

IPAddress subnet(255, 255, 255, 0); //子网掩码

IPAddress dns(8, 8, 8, 8); //dns 服务器，默认

const char *deviceName = "D1_esp8266"; //为设备在网络中取个名字，在路由器中可以查看到

const char *ssid = "New_Best_wifi";
const char *password = "12345678";

void connect_to_wifi()
{
    WiFi.disconnect(); //防止使用以前的配置连接WiFi
    WiFi.hostname(deviceName);
    WiFi.config(staticIP, gateway, subnet, dns);
    Serial.println("setting wifi mode");
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    Serial.printf("Connecting to %s", ssid);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.print("Connected,IP address:");
    Serial.println(WiFi.localIP());
}
