% McDermott
% 06 Jan 2016
% sandia_helium_plume.m

close all
clear all

expdir = '../Experimental_Data/';
cmpdir = '../Computational_Results/';
pltdir = '../Plots/';
addpath '../../../Utilities/'
plot_style

chid = {'Sandia_He_1m_p2','Sandia_He_1m_p4','Sandia_He_1m_p6'};
expxhdr = {'x (m)','x (m)','x (m)'};
expyhdr = {'Y He','Y He rms','U (m/s)','U rms (m/s)','W (m/s)','W rms (m/s)'};
exp_marker_style = {'ko','ko','ro','ro','bo','bo'};

title1 = {'Sandia Helium Plume','Sandia Helium Plume','Sandia Helium Plume'};
title2 = {'z = 0.2 m','z = 0.4 m','z = 0.6 m'};
xlbl = {'x (m)','x (m)','x (m)'};
ylbl = {'Helium Mass Fraction','RMS Helium Mass Fraction','Radial Velocity (m/s)','RMS Radial Velocity (m/s)','Vertical Velocity (m/s)','RMS Verticel Velocity (m/s)'};
pltid = {'_YHe','_YHerms','_U','_Urms','_W','_Wrms'};

% Experimental error (rel_error) is taken from Sec. II of
%
% Desjardin et al. Large-eddy simulation and experimental measurements of the near-field of a large turbulent helium plume.
% Physics of Fluids, Vol. 16, No. 6, June 2004.

rel_error =[.23,.21,.2,.3,.2,.3];

% format axis range and ticks

xmin = [-.5 -.5 -.5];  xmax = [ .5  .5  .5];   dx = [.1 .1 .1];
ymin = [0 0 -1 0 0 0]; ymax = [1 .25 1 1 5 2]; dy = [.2 .05 .25 .25 1 .25];

data_stride = 4; % skip this number of points for readability

for i=1:length(chid)

    % import experimental data

    E1 = importdata([expdir,chid{i},'.csv'],',',1);

    x1 = E1.data(1:data_stride:end,find(strcmp(E1.colheaders,expxhdr{i})));

    for j=1:length(expyhdr)

        figure; hold off

        y1 = E1.data(1:data_stride:end,find(strcmp(E1.colheaders,expyhdr{j})));
        plot(x1,y1,exp_marker_style{j},'MarkerSize',Marker_Size); hold on

        % add error bars

        e = rel_error(j)*abs(y1);
        H(1)=errorbar(x1,y1,-e,+e,exp_marker_style{j},'MarkerSize',Marker_Size);

        % plot computational results *********************************
        
        % add your results here!

        % ************************************************************

        xt = xmin(i) + .05*(xmax(i)-xmin(i));
        yt = ymin(j) + .92*(ymax(j)-ymin(j));
        text(xt,yt,title1{i},'FontSize',Font_Size)

        xt = xmin(i) + .05*(xmax(i)-xmin(i));
        yt = ymin(j) + .84*(ymax(j)-ymin(j));
        text(xt,yt,title2{i},'FontSize',Font_Size)

        axis([xmin(i) xmax(i) ymin(j) ymax(j)])
        set(gca,'YTick',ymin(j):dy(j):ymax(j))
        set(gca,'YMinorTick','on')
        set(gca,'XTick',xmin(i):dx(i):xmax(i))
        set(gca,'XMinorTick','on')
        set(gca,'FontSize',Font_Size)
        xlabel(xlbl{i},'FontSize',Font_Size)
        ylabel(ylbl{j},'FontSize',Font_Size)
        lh = legend(H,'Exp','Location','NorthEast');
        set(lh,'FontSize',Font_Size)
        legend 'boxoff'

        loose_inset
        print(gcf,'-dpdf',[pltdir,chid{i},pltid{j}])

    end

end
