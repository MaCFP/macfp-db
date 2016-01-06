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

expfilename = {'Sandia_He_1m_p2.csv','Sandia_He_1m_p4.csv','Sandia_He_1m_p6.csv'};
expxhdr = {'x (m)','x (m)','x (m)'};
expyhdr = {'Y He','Y He rms','U (m/s)','U rms (m/s)','W (m/s)','W rms (m/s)'};
exp_marker_style = {'ko','ko','ro','ro','bo','bo'};

title1 = {'Sandia Helium Plume','Sandia Helium Plume','Sandia Helium Plume'};
title2 = {'z = 0.2 m','z = 0.4 m','z = 0.6 m'};
xlbl = {'x (m)','x (m)','x (m)'};
ylbl = {'Helium Mass Fraction','RMS Helium Mass Fraction','Radial Velocity (m/s)','RMS Radial Velocity (m/s)','Vertical Velocity (m/s)','RMS Verticel Velocity (m/s)'};

xmin = [-.5 -.5 -.5];
xmax = [ .5  .5  .5];
ymin = [0 0  -1 0 0 0];
ymax = [1 .25 1 1 5 2];

data_stride = 4; % skip this number of points for readability

for i=1:length(expfilename)

    % import experimental data

    E1 = importdata([expdir,expfilename{i}],',',1);

    x1 = E1.data(:,find(strcmp(E1.colheaders,expxhdr{i})));

    for j=1:length(expyhdr)

        figure

        y1 = E1.data(:,find(strcmp(E1.colheaders,expyhdr{j})));

        H(1)=plot(x1(1:data_stride:end),y1(1:data_stride:end),exp_marker_style{j},'MarkerSize',Marker_Size);

        % % plot computational results *********************************
        
        % % add your results here!

        % hold on
        % C1 = importdata([cmpdir,cmpfilename{i}],',',1);
        % x1 = C1.data(:,find(strcmp(C1.colheaders,cmpxhdr{i})));
        % y1 = C1.data(:,find(strcmp(C1.colheaders,cmpyhdr{i})));

        % H(2)=plot(x1,y1,cmp_marker_style{i},'MarkerSize',Marker_Size);

        % % ************************************************************

        xt = xmin(i) + .03*(xmax(i)-xmin(i));
        yt = ymin(j) + .92*(ymax(j)-ymin(j));
        text(xt,yt,title1{i},'FontSize',Font_Size)

        xt = xmin(i) + .03*(xmax(i)-xmin(i));
        yt = ymin(j) + .84*(ymax(j)-ymin(j));
        text(xt,yt,title2{i},'FontSize',Font_Size)

        axis([xmin(i) xmax(i) ymin(j) ymax(j)])
        set(gca,'FontSize',Font_Size)
        xlabel(xlbl{i},'FontSize',Font_Size)
        ylabel(ylbl{j},'FontSize',Font_Size)
        % lh = legend(H,'Exp','Cmp','Location',legloc{i});
        % set(lh,'FontSize',Font_Size)

        % loose_inset
        % print(gcf,'-dpdf',[pltdir,plotname{i}])

    end

end
