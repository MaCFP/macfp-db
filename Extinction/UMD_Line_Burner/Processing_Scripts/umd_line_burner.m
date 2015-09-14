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

filename = {'Exp_O2_p18_T_z_p125m.csv','Exp_O2_p18_T_z_p250m.csv','Exp_O2_p18_O2_z_p125m.csv','Exp_O2_p18_O2_z_p250m.csv'};
xhdr = {'x (m)','x (m)','x (m)','x (m)'};
yhdr = {'T (C)','T (C)','O2 (vol frac)','O2 (vol frac)'};
marker_style = {'ksq','ksq','ko','ko'};
title1 = {'UMD Line Burner, CH4','UMD Line Burner, CH4','UMD Line Burner, CH4','UMD Line Burner, CH4'};
title2 = {'18 % O2, z = 0.125 m','18 % O2, z = 0.250 m','18 % O2, z = 0.125 m','18 % O2, z = 0.250 m'};
xlbl = {'Position (m)','Position (m)','Position (m)','Position (m)'};
ylbl = {'Thermocouple Temperature ( \circC )','Thermocouple Temperature ( \circC )','O2 (vol frac)','O2 (vol frac)'};
plotname = {'methane_O2_p18_TC_z_p125','methane_O2_p18_TC_z_p250','methane_O2_p18_O2_z_p125','methane_O2_p18_O2_z_p250'};
xmin = [-.25,-.25,-.25,-.25];
xmax = [ .25, .25, .25, .25];
ymin = [0,0,.05,.05];
ymax = [1200,1200,.25,.25];

for i=1:length(filename)

    figure

    M1 = importdata([expdir,filename{i}],',',1);

    x1 = M1.data(:,find(strcmp(M1.colheaders,xhdr{i})));
    y1 = M1.data(:,find(strcmp(M1.colheaders,yhdr{i})));

    H(1)=plot(x1,y1,marker_style{i},'MarkerSize',Marker_Size); % hold on

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
    lh = legend(H,'Exp');
    set(lh,'FontSize',Font_Size)

    loose_inset
    print(gcf,'-dpdf',[pltdir,plotname{i}])

end
