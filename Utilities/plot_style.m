% McDermott
% 14 Sep 2015
% plot_style.m
%
% Preferred style for MaCFP plots
% Usage: When creating a new figure use the following:
%
% plot_style
% figure
% set(gca,'Units',Plot_Units)
% set(gca,'Position',[Plot_X Plot_Y Plot_Width Plot_Height])
%
% ==>> plot(X,Y,etc)
% ==>> xlabel(Ind_Title,'Interpreter',Font_Interpreter,'FontSize',Label_Font_Size)
% ==>> ylabel(Dep_Title,'Interpreter',Font_Interpreter,'FontSize',Label_Font_Size)
%
% set(gca,'FontName',Font_Name)
% set(gca,'FontSize',Label_Font_Size)
%
% ==>> lh=legend(...);
% ==>> set(lh,'FontName',Font_Name,'FontSize',Key_Font_Size)
%
% set(gcf,'Visible',Figure_Visibility);
% set(gcf,'Units',Paper_Units);
% set(gcf,'PaperSize',[Paper_Width Paper_Height]);
% set(gcf,'Position',[0 0 Paper_Width Paper_Height]);
% print(gcf,'-dpdf',plotname);

% Font properties
Font_Name = 'Helvetica'; %get(gca,'fontname')
Font_Interpreter = 'TeX';
Font_Size       = 20;
Key_Font_Size   = 20;
Title_Font_Size = 20;
Label_Font_Size = 20;
Marker_Size = 12;

% Line properties
Line_Width      = 2; % get(gca,'linewidth')

% Plot properties
Plot_Units      = 'normalized'; %get(gca,'units')
Pos             = [0.1500    0.1500    0.7750    0.8150]; %get(gca,'position') % [left bottom width height]
YLabel_Offset   = -0.05; % normalized units
XLabel_Offset   = -0.05; % normalized units
Plot_X          = Pos(1);
Plot_Y          = Pos(2);
Plot_Width      = Pos(3);
Plot_Height     = Pos(4); %*.95; % use for exponential notation on y-axis tick labels

% Paper properties
Paper_Units     = 'inches'; %get(gcf,'paperunits')
Paper_Pos       = [0.2500    2.5000    8.0000    6.0000]; %get(gcf,'paperposition')
Paper_Width     = Paper_Pos(3);
Paper_Height    = Paper_Pos(4);

% Print properties
Figure_Visibility = 'on';
Image_File_Type = '-dpdf';
