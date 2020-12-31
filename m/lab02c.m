wclear
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

batt = 0;
n = 10;
a = 0;
b = 0;
c = 0;
d = 0;
e = 0;
f = 0;
g = 0;

battd = 1000;


for i = 1:365
    j = 3;
    min = floor(w(i));
    max = ceil(w(i));
    if w(i) == 0;
        P(i) = 0;
    else
        P(i) = n*(((w(i) - min) / (max - min))*(p(j,max+1)-p(j,min+1))+p(j,min+1));
    end

    cd(i) = (P(i) - l(i));

    if P(i) > l(i)
%         f = f + 1;
        if i == 1
            a = a + 1;
            batti(i) = P(i) - l(i);
            battt(i) = batti(i);
        else
            b = b + 1;
            batti(i) = P(i) - l(i);
            battt(i) = batti(i) + battt(i-1);
        end
    elseif P(i) == l(i)
        c = c + 1;
        batti(i) = 0;
        battt(i) = battt(i-1);
    else
        g = g + 1;
        if i == 1
            d = d + 1;
            battt(i) = 0;
        else
            e = e + 1;
            if battt(i-1) > (l(i) - P(i))
                battt(i) = battt(i-1) - (l(i) - P(i));
            elseif battt(i-1) < (l(i) - P(i))
                battt(i) = 0;
            else
                battt(i) = 0;
            end
        end
    end
end
tot = a + b + c + e + f + g
Turbine_Power_kWh = sum(P)*365*24
Load_kWh = sum(l)*365*24

% discharge_max = min(cd(:))
% charge = max(P)

for i = 1:365
    if i == 1
        max = cd(i);
        min = cd(i);
    end
    if cd(i) > max
        max = cd(i);
    end
    if cd(i) < min
        min = cd(i);
    end
end

Power_min = min
Power_max = max

for i = 1:365
    if i == 1
        max = battt(i);
        min = battt(i);
    end
    if battt(i) > max
        max = battt(i);
    end
    if battt(i) < min
        min = battt(i);
    end
end

Energy_max = max

plot(t,l,t,P,t,battt)
title('Masirah Average Load Profile')
xlim([1 365])
xlabel('Days')
ylabel('Average Load (kW)')
legend('Load (kW)','Turbine (kW)','Battery (kWh)')
