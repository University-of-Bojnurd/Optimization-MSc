

clc
clear all
close all
a=[0,4,2,1,2];
b=[1,2,3,2,4];
w=[2,4,1,3,2];
x=0:0.01:4;
y=1:0.01:4;
[X,Y]=meshgrid(x,y);
Z=2*(abs(X-0)+abs(Y-1))+4*(abs(X-4)+abs(Y-2))+1*(abs(X-2)+abs(Y-3))+3*(abs(X-1)+abs(Y-2))+2*(abs(X-2)+abs(Y-4));
contour(X,Y,Z)
surfc(X,Y,Z)






%% روش حل پله ای یا متعامد 
%% در نرم افزار متلب
%% Matlab.



