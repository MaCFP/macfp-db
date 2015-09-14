% McDermott
% 14 Sep 2015
% umd_line_burner

close all
clear all

expdir = '../Experimental_Data/';
cmpdir = '../Computational_Results/';
pltdir = '../Plots/';
addpath '../../../Utilities/'
plot_style

expfilename = {'Exp_O2_p18_T_z_p125.csv','Exp_O2_p18_T_z_p250.csv','Exp_O2_p18_O2_z_p125.csv','Exp_O2_p18_O2_z_p250.csv'};
expxhdr = {'x (m)','x (m)','x (m)','x (m)'};
expyhdr = {'T (C)','T (C)','O2 (vol frac)','O2 (vol frac)'};
exp_marker_style = {'ksq','ksq','ko','ko'};

cmpfilename = {'methane_O2_p18_TC_z_p125_example.csv','methane_O2_p18_TC_z_p250_example.csv','methane_O2_p18_O2_z_p125_example.csv','methane_O2_p18_O2_z_p250_example.csv'};
cmpxhdr = {'x (m)','x (m)','x (m)','x (m)'};
cmpyhdr = {'T (C)','T (C)','O2 (vol frac)','O2 (vol frac)'};
cmp_marker_style = {'b-','b-','r-','r-'};

title1 = {'UMD Line Burner, CH4','UMD Line Burner, CH4','UMD Line Burner, CH4','UMD Line Burner, CH4'};
title2 = {'18 % O2, z = 0.125 m','18 % O2, z = 0.250 m','18 % O2, z = 0.125 m','18 % O2, z = 0.250 m'};
xlbl = {'Position (m)','Position (m)','Position (m)','Position (m)'};
ylbl = {'Thermocouple Temperature ( \circC )','Thermocouple Temperature ( \circC )','O2 (vol frac)','O2 (vol frac)'};
plotname = {'methane_O2_p18_TC_z_p125','methane_O2_p18_TC_z_p250','methane_O2_p18_O2_z_p125','methane_O2_p18_O2_z_p250'};
xmin = [-.25,-.25,-.25,-.25];
xmax = [ .25, .25, .25, .25];
ymin = [0,0,.05,.05];
ymax = [1200,1200,.25,.25];
legloc = {'northeast','northeast','southeast','southeast'};

for i=1:length(expfilename)

    figure

    % plot experimental data

    E1 = importdata([expdir,expfilename{i}],',',1);

    x1 = E1.data(:,find(strcmp(E1.colheaders,expxhdr{i})));
    y1 = E1.data(:,find(strcmp(E1.colheaders,expyhdr{i})));

    H(1)=plot(x1,y1,exp_marker_style{i},'MarkerSize',Marker_Size);

    % plot computational results *********************************
    
    % add your results here!

    hold on
    C1 = importdata([cmpdir,cmpfilename{i}],',',1);
    x1 = C1.data(:,find(strcmp(C1.colheaders,cmpxhdr{i})));
    y1 = C1.data(:,find(strcmp(C1.colheaders,cmpyhdr{i})));

    H(2)=plot(x1,y1,cmp_marker_style{i},'MarkerSize',Marker_Size);

    % ************************************************************

    xt = xmin(i) + .03*(xmax(i)-xmin(i));
    yt = ymin(i) + .92*(ymax(i)-ymin(i));
    text(xt,yt,title1{i},'FontSize',Font_Size)

    xt = xmin(i) + .03*(xmax(i)-xmin(i));
    yt = ymin(i) + .84*(ymax(i)-ymin(i));
    text(xt,yt,title2{i},'FontSize',Font_Size)

    axis([xmin(i) xmax(i) ymin(i) ymax(i)])
    set(gca,'FontSize',Font_Size)
    xlabel(xlbl{i},'FontSize',Font_Size)
    ylabel(ylbl{i},'FontSize',Font_Size)
    lh = legend(H,'Exp','Cmp','Location',legloc{i});
    set(lh,'FontSize',Font_Size)

    loose_inset
    print(gcf,'-dpdf',[pltdir,plotname{i}])

end
