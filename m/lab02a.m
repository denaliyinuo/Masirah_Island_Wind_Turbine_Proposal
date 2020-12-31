clear
clc

A = xlsread('data.xlsx');

wo = A(:,3);
lo = A(:,4);
t = [1:1:365];

E33p = [0,0,0,5,13.7,30,55,92,138,196,250,292.8,320,335];
E44p = [0,0,1.4,8,24.5,53,96,156,238,340,466,600,710,790];
E48p = [0,0,2,12,32,66,120,191,284,405,555,671,750,790];
E53p = [0,0,2,14,38,77,141,228,336,480,645,744,780,810];
E70p = [0,0,2,18,56,127,240,400,626,892,1223,1590,1900,2080];
E82p = [0,0,3,25,82,174,321,532,815,1180,1612,1890,2000,2050];

E33c = [0,0,0,.35,.4,.45,.47,.5,.5,.5,.47,.41,.35,.28];
E44c = [0,0,.19,.32,.41,.46,.48,.49,.5,.5,.5,.48,.44,.39];
E48c = [0,0,.23,.4,.45,.48,.5,.5,.5,.5,.5,.45,.39,.32];
E53c = [0,0,.19,.39,.44,.46,.48,.49,.49,.49,.48,.42,.34,.27];
E70c = [0,0,.1,.27,.36,.42,.46,.48,.5,.5,.5,.49,.45,.39];
E82c = [0,0,.12,.29,.4,.43,.46,.48,.49,.5,.5,.44,.36,.29];

p = [E33p;E44p;E48p;E53p;E70p;E82p];
e = [E33c;E44c;E48c;E53c;E70c;E82c];
Pt = 0;
n = 0;
z = 0;

for i = 1:365
    w(i) = wo(i);
    l(i) = lo(i);
end

for j = 1:6
    Pt = 0;
    efft = 0;
    for i = 1:365
        if w(i) == 0
            z = z + 1;
            P = 0;
            diff(j,i) = P - l(i);
        else
            n = n + 1;
            min = floor(w(i));
            max = ceil(w(i));
            P = ((w(i) - min) / (max - min))*(p(j,max+1)-p(j,min+1))+p(j,min+1);
            diff(j,i) = P - l(i);
            Pt = Pt + P;
            eff = ((w(i) - min) / (max - min))*(e(j,max+1)-e(j,min+1))+e(j,min+1);
            efft = efft + eff;
            if j == 3
                P_EE48(i) = ((w(i) - min) / (max - min))*(p(j,max+1)-p(j,min+1))+p(j,min+1);
            end
        end
    end
end

% subplot(2,1,1)
% plot(t,w)
% 
% subplot(2,1,2)
plot(t,l,t,l-P_EE48*3,t,P_EE48*3)
title('Masirah Power Generation Profile of Eight 1 MW Diesel Generators and Three E48 Wind Turbines')
xlim([1 365])
ylim([0 8000])
xlabel('Days')
ylabel('Power (kW)')
legend('Load','Eight 1 MW Generators','Three E48 Turbines','best')
