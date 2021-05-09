#include <stdio.h>

#include <stdlib.h>

#include <string.h>

#include <unistd.h>

#include <sys/socket.h>

#include <netinet/in.h>

#include <arpa/inet.h>

int main (void)

{

char IPdotdec[20]; //存放点分十进制IP地址
//unsigned int IPv4;

struct in_addr s; // IPv4地址结构体

// 输入IP地址

printf("Please input IPv4: ");

scanf("%x", &s.s_addr);

//s.s_addr = IPv4;


// 反转换
//在这里调用了函数ntonl将字节顺序换成了主机字节顺序
s.s_addr = ntohl(s.s_addr);
inet_ntop(AF_INET, (void *)&s,IPdotdec,16);

printf("inet_ntop: %s\n", IPdotdec);

}


