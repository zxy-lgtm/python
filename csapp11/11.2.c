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

struct in_addr s; // IPv4地址结构体

// 输入IP地址

printf("Please input IP address: ");

scanf("%s", IPdotdec);

// 转换

inet_pton(AF_INET, IPdotdec, (void *)&s);//该函数得到的字节顺序为主机字节顺序，即小端顺序

//在这里调用了函数htonl将字节顺序换成了网络字节顺序
s.s_addr = htonl(s.s_addr);
printf("inet_pton: 0x%x\n", s.s_addr);

// 反转换
//在这里调用了函数ntonl将字节顺序换成了主机字节顺序
s.s_addr = ntohl(s.s_addr);
inet_ntop(AF_INET, (void *)&s, IPdotdec, 16);

printf("inet_ntop: %s\n", IPdotdec);

}


