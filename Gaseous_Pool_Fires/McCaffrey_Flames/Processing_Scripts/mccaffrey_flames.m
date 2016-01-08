% McDermott
% 08 Jan 2016
% mccaffrey_flames.m

close all
clear all

expdir = '../Experimental_Data/';
cmpdir = '../Computational_Results/';
pltdir = '../Plots/';
addpath '../../../Utilities/'
plot_style

Q = [14.4 21.7 33.0 44.9 57.5]; % kW [14.4 21.7 33.0 44.9 57.5]
g = 9.8;
rho = 1.18;
cp = 1;
T0 = 273.15 + 20;

DS = (Q/(rho*cp*T0*sqrt(g))).^(2/5); % m

chid = {'McCaffrey_14kW','McCaffrey_22kW','McCaffrey_33kW','McCaffrey_45kW','McCaffrey_57kW'};
mark = {'ko','k+','k^','ksq','kd'};
n_chid = length(chid);

% McCaffrey plume correlations NBSIR 79-1910

zq = logspace(-2,0,100);

for i=1:length(zq)
    if zq(i)<0.08
        vq(i) = 6.84*zq(i)^0.5;
        Tq(i) = 800*zq(i)^0;
    elseif zq(i)>=0.08 & zq(i)<=0.2
        vq(i) = 1.93*zq(i)^0;
        Tq(i) = 63*zq(i)^(-1);
    elseif zq(i)>0.2
        vq(i) = 1.12*zq(i)^(-1/3);
        Tq(i) = 21.6*zq(i)^(-5/3);
    end
end

h1 = zeros(1,length(chid)+1);
h2 = zeros(1,length(chid)+1);

figure(1); h1(end)=loglog(zq,vq,'r--','linewidth',2); hold on
figure(2); h2(end)=loglog(zq,Tq,'b--','linewidth',2); hold on

for i=1:length(chid)
    V = importdata([expdir,chid{i},'_V.csv'],',',1);
    T = importdata([expdir,chid{i},'_T.csv'],',',1);
    figure(1); h1(i)=loglog(V.data(:,1),V.data(:,2),mark{i});
    figure(2); h2(i)=loglog(T.data(:,1),T.data(:,2),mark{i});
end

% format and print velocity correlation

figure(1)
xlabel('z/Q^{2/5}','FontSize',Font_Size)
ylabel('V/Q^{1/5}','FontSize',Font_Size)
title('McCaffrey Centerline Velocity Correlation','FontSize',Font_Size)

xmin = 0.01;
xmax = 1;
ymin = 0.3;
ymax = 2.5;
axis([xmin xmax ymin ymax])

lh = legend(h1,'14.4 kW','21.7 kW','33.0 kW','44.9 kW','57.5 kW','(z/Q^{2/5})^\eta','Location','SouthEast');
set(lh,'FontSize',Font_Size)
legend 'boxoff'

text(.04,1.2,'\eta=1/2','FontSize',Font_Size)
text(.10,1.7,'\eta=0','FontSize',Font_Size)
text(.295,1.25,'\eta=-1/3','FontSize',Font_Size)

loose_inset
print(gcf,'-dpdf',[pltdir,'McCaffrey_Velocity_Correlation'])

% format and print temperature correlation

figure(2)
xlabel('z/Q^{2/5}','FontSize',Font_Size)
ylabel('\DeltaT (^\circC)','FontSize',Font_Size)
title('McCaffrey Centerline Temperature Correlation','FontSize',Font_Size)

axis([.008 1 40 1000])

lh = legend(h2,'14.4 kW','21.7 kW','33.0 kW','44.9 kW','57.5 kW','(z/Q^{2/5})^\eta','Location','SouthWest');
set(lh,'FontSize',Font_Size)
legend 'boxoff'

text(.03,650,'\eta=0','FontSize',Font_Size)
text(.08,425,'\eta=-1','FontSize',Font_Size)
text(.18,125,'\eta=-5/3','FontSize',Font_Size)

loose_inset
print(gcf,'-dpdf',[pltdir,'McCaffrey_Temperature_Correlation'])

return



% % Baum and McCaffrey plume correlations (in terms of D*)
% % 2nd IAFSS, pp. 129-148

% zs = logspace(-2,1,100);
% n = [1/2 0 -1/3];
% A = [2.18 2.45 3.64];
% B = [2.91 3.81 8.41];

% for i=1:length(zs)
%     if zs(i)<1.32
%         j=1;
%     elseif zs(i)>=1.32 & zs(i)<=3.3
%         j=2;
%     elseif zs(i)>3.3
%         j=3;
%     end
%     us(i) = A(j)*zs(i)^n(j);
%     Ts(i) = B(j)*zs(i)^(2*n(j)-1);
% end
