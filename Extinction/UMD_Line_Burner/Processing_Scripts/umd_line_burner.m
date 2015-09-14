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

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% % mean temperature at z=0.250 m
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% figure
% plot_style

% M1 = importdata([expdir,'Exp_O2_p18_T_z_p250m.csv'],',',1);

% y1 = M1.data(:,find(strcmp(M1.colheaders,'y (m)')));
% T1 = M1.data(:,find(strcmp(M1.colheaders,'T (C)')));

% H(1)=plot(y1,T1,'ksq','MarkerSize',Marker_Size); hold on

% % find 18 % O2 time block

% t1 = F1.data(:,1); t1range = find(t1>=30 & t1<=40);
% t2 = F2.data(:,1); t2range = find(t2>=30 & t2<=40);
% %t3 = F3.data(:,1); t3range = find(t3>=30 & t3<=40);

% C1 = 3;
% ND1 = 40;
% TG1_p250 = C1+3*ND1:C1+4*ND1-1;
% TC1_p250 = C1+4*ND1:C1+5*ND1-1;

% C2 = 3;
% ND2 = 80;
% TG2_p250 = C2+3*ND2:C2+4*ND2-1;
% TC2_p250 = C2+4*ND2:C2+5*ND2-1;

% % C3 = 3;
% % ND3 = 160;
% % TG3_p250 = C3+3*ND3:C3+4*ND3-1;
% % TC3_p250 = C3+4*ND3:C3+5*ND3-1;

% TG1 = mean(F1.data(t1range,TG1_p250),1);
% TC1 = mean(F1.data(t1range,TC1_p250),1);

% TG2 = mean(F2.data(t2range,TG2_p250),1);
% TC2 = mean(F2.data(t2range,TC2_p250),1);

% % TG3 = mean(F3.data(t3range,TG3_p250),1);
% % TC3 = mean(F3.data(t3range,TC3_p250),1);

% H(2) = plot(yc1,TC1,'r-.','LineWidth',Line_Width); % dx = 1.25 cm
% H(3) = plot(yc2,TC2,'m--','LineWidth',Line_Width);  % dx = 0.625 cm
% %H(4) = plot(yc3,TC3,'b-','LineWidth',Line_Width);  % dx = 0.3125 cm

% xmin = -0.25;
% xmax = 0.25;
% ymin = 0;
% ymax = 1200;
% xt = xmin + .03*(xmax-xmin);
% yt = ymin + .92*(ymax-ymin);
% text(xt,yt,'UMD Gas Burner - CH4','FontName',Font_Name,'FontSize',Title_Font_Size,'Interpreter',Font_Interpreter)
% xt = xmin + .03*(xmax-xmin);
% yt = ymin + .84*(ymax-ymin);
% text(xt,yt,'18 % O2, z = 0.250 m','FontName',Font_Name,'FontSize',Title_Font_Size,'Interpreter',Font_Interpreter)

% axis([xmin xmax ymin ymax])
% xlabel('Position (m)')
% ylabel('Thermocouple Temperature ( \circC )')
% legend(H,'Exp','FDS 1.25 cm','FDS 0.625 cm') %,'FDS 0.3125 cm')

% % add SVN if file is available

% git_file = [fdsdir,'methane_dx_1p25cm_git.txt'];
% addverstr(gca,git_file,'linear')

% % print to pdf
% print(gcf,'-dpdf',[pltdir,'methane_O2_p18_TC_z_p250'])

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% % O2 concentration at z=0.125 m
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% figure
% plot_style

% M1 = importdata([expdir,'Exp_O2_p18_O2_z_p125m.csv'],',',1);

% y1 = M1.data(:,find(strcmp(M1.colheaders,'y (m)')));
% O21 = M1.data(:,find(strcmp(M1.colheaders,'O2 (vol frac)')));

% H(1)=plot(y1,O21,'ko','MarkerSize',Marker_Size); hold on

% % find 18 % O2 time block

% t1 = F1.data(:,1); t1range = find(t1>=30 & t1<=40);
% t2 = F2.data(:,1); t2range = find(t2>=30 & t2<=40);
% %t3 = F3.data(:,1); t3range = find(t3>=30 & t3<=40);

% C1 = 3;
% ND1 = 40;
% O21_p125 = C1+2*ND1:C1+3*ND1-1;

% C2 = 3;
% ND2 = 80;
% O22_p125 = C2+2*ND2:C2+3*ND2-1;

% % C3 = 3;
% % ND3 = 160;
% % O23_p125 = C3+2*ND3:C3+3*ND3-1;

% % z = 0.125 m

% O2_1 = mean(F1.data(t1range,O21_p125),1);
% O2_2 = mean(F2.data(t2range,O22_p125),1);
% %O2_3 = mean(F3.data(t3range,O23_p125),1);

% H(2) = plot(yc1,O2_1,'r-.','LineWidth',Line_Width); % dx = 1.25 cm
% H(3) = plot(yc2,O2_2,'m--','LineWidth',Line_Width);  % dx = 0.625 cm
% %H(4) = plot(yc3,O2_3,'b-','LineWidth',Line_Width);  % dx = 0.3125 cm

% xmin = -0.25;
% xmax = 0.25;
% ymin = 0.05;
% ymax = 0.25;
% xt = xmin + .03*(xmax-xmin);
% yt = ymin + .92*(ymax-ymin);
% text(xt,yt,'UMD Gas Burner - CH4','FontName',Font_Name,'FontSize',Title_Font_Size,'Interpreter',Font_Interpreter)
% xt = xmin + .03*(xmax-xmin);
% yt = ymin + .84*(ymax-ymin);
% text(xt,yt,'18 % O2, z = 0.125 m','FontName',Font_Name,'FontSize',Title_Font_Size,'Interpreter',Font_Interpreter)

% axis([xmin xmax ymin ymax])
% xlabel('Position (m)')
% ylabel('O2 (vol frac)')
% legend(H,'Exp','FDS 1.25 cm','FDS 0.625 cm') %,'FDS 0.3125 cm','Location','Southwest')

% % add SVN if file is available

% git_file = [fdsdir,'methane_dx_1p25cm_git.txt'];
% addverstr(gca,git_file,'linear')

% % print to pdf
% print(gcf,'-dpdf',[pltdir,'methane_O2_p18_O2_z_p125'])

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% % O2 concentration at z=0.250 m
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% figure
% plot_style

% M1 = importdata([expdir,'Exp_O2_p18_O2_z_p250m.csv'],',',1);

% y1 = M1.data(:,find(strcmp(M1.colheaders,'y (m)')));
% O21 = M1.data(:,find(strcmp(M1.colheaders,'O2 (vol frac)')));

% H(1)=plot(y1,O21,'ko','MarkerSize',Marker_Size); hold on

% % find 18 % O2 time block

% t1 = F1.data(:,1); t1range = find(t1>=30 & t1<=40);
% t2 = F2.data(:,1); t2range = find(t2>=30 & t2<=40);
% %t3 = F3.data(:,1); t3range = find(t3>=30 & t3<=40);

% C1 = 3;
% ND1 = 40;
% O21_p250 = C1+5*ND1:C1+6*ND1-1;

% C2 = 3;
% ND2 = 80;
% O22_p250 = C2+5*ND2:C2+6*ND2-1;

% % C3 = 3;
% % ND3 = 160;
% % O23_p250 = C3+5*ND3:C3+6*ND3-1;

% % z = 0.125 m

% O2_1 = mean(F1.data(t1range,O21_p250),1);
% O2_2 = mean(F2.data(t2range,O22_p250),1);
% %O2_3 = mean(F3.data(t3range,O23_p250),1);

% H(2) = plot(yc1,O2_1,'r-.','LineWidth',Line_Width); % dx = 1.25 cm
% H(3) = plot(yc2,O2_2,'m--','LineWidth',Line_Width);  % dx = 0.625 cm
% %H(4) = plot(yc3,O2_3,'b-','LineWidth',Line_Width);  % dx = 0.3125 cm

% xmin = -0.25;
% xmax = 0.25;
% ymin = 0.05;
% ymax = 0.25;
% xt = xmin + .03*(xmax-xmin);
% yt = ymin + .92*(ymax-ymin);
% text(xt,yt,'UMD Gas Burner - CH4','FontName',Font_Name,'FontSize',Title_Font_Size,'Interpreter',Font_Interpreter)
% xt = xmin + .03*(xmax-xmin);
% yt = ymin + .84*(ymax-ymin);
% text(xt,yt,'18 % O2, z = 0.250 m','FontName',Font_Name,'FontSize',Title_Font_Size,'Interpreter',Font_Interpreter)

% axis([xmin xmax ymin ymax])
% xlabel('Position (m)')
% ylabel('O2 (vol frac)')
% legend(H,'Exp','FDS 1.25 cm','FDS 0.625 cm') %,'FDS 0.3125 cm','Location','Southwest')

% % add SVN if file is available

% git_file = [fdsdir,'methane_dx_1p25cm_git.txt'];
% addverstr(gca,git_file,'linear')

% % print to pdf
% print(gcf,'-dpdf',[pltdir,'methane_O2_p18_O2_z_p250'])





