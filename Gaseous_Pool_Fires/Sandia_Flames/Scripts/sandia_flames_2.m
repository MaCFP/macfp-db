% McDermott
% 02 May 2017
% sandia_flames_2.m

close all
clear all

expdir = '../Experimental_Data/';
cmpdir = '../Computational_Results/2017/';
pltdir = '../Plots/';
addpath '../../../Utilities/'
plot_style

% read exp data configuration file
Exp = importdata([expdir,'dataplot_inputs.csv']);
Exp_H = textscan(Exp{1},'%q','delimiter',',');
Exp_headers = Exp_H{:}'; clear Exp_H
n_plots = length(Exp);

% get list of participants
inst = get_folder_list(cmpdir);
n_inst = length(inst);
for n = 1:n_inst
    Cmp{n} = importdata([cmpdir,inst{n},'/',inst{n},'_dataplot_inputs.csv']); % this file maps cmp data file to exp data file
    Cmp_H = textscan(Cmp{n}{1},'%q','delimiter',',');
    Cmp_headers{n} = Cmp_H{:}'; clear Cmp_H
end

for i=2:n_plots

    if i>n_plots; break; end

    figure

    % load experimental data

    P = textscan(Exp{i},'%q','delimiter',',');
    Exp_params = P{:}';

    Exp_Filename      = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Data_Filename')))));
    Exp_x_Col_Name    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'x_Col_Name')))));
    Exp_y_Col_Name    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'y_Col_Name')))));
    Exp_Legend_Key    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Legend_Key')))));
    Exp_Plot_Style    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Plot_Style')))));

    xLabel            = strtrim(char(Exp_params(find(strcmp(Exp_headers,'xLabel')))));
    yLabel            = strtrim(char(Exp_params(find(strcmp(Exp_headers,'yLabel')))));
    xMin              = str2num(char(Exp_params(find(strcmp(Exp_headers,'xMin')))));
    xMax              = str2num(char(Exp_params(find(strcmp(Exp_headers,'xMax')))));
    yMin              = str2num(char(Exp_params(find(strcmp(Exp_headers,'yMin')))));
    yMax              = str2num(char(Exp_params(find(strcmp(Exp_headers,'yMax')))));
    xTick             = str2num(char(Exp_params(find(strcmp(Exp_headers,'xTick')))));
    yTick             = str2num(char(Exp_params(find(strcmp(Exp_headers,'yTick')))));
    Legend_Location   = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Legend_Location')))));
    Plot_Filename     = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Plot_Filename')))));
    Plot_Title        = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Plot_Title')))));

    E = importdata([expdir,Exp_Filename],',',1);

    X1 = E.data(:,find(strcmp(strtrim(E.colheaders),Exp_x_Col_Name)));
    Y1 = E.data(:,find(strcmp(strtrim(E.colheaders),Exp_y_Col_Name)));

    H(1)=plot(X1,Y1,Exp_Plot_Style,'MarkerSize',Marker_Size); hold on
    n_key=1;
    Legend_Key{n_key} = Exp_Legend_Key;

    % load computational data from each institution

    for n=1:n_inst

        % scan the Cmp list associated with Exp_Filename and Exp_y_Col_Name

        Exp_Filename_Col = find(strcmp(strtrim(Cmp_headers{n}),'Exp_Filename'));
        Cmp_Filename_Col = find(strcmp(strtrim(Cmp_headers{n}),'Cmp_Filename'));
        Exp_y_Col_Index  = find(strcmp(strtrim(Cmp_headers{n}),'Exp_y_Col_Name'));

        for k=2:length(Cmp{n})
            M = textscan(Cmp{n}{k},'%q','delimiter',',');
            Cmp_params = M{:}';
            if strcmp(strtrim(Cmp_params(Exp_Filename_Col)),Exp_Filename) & strcmp(strtrim(Cmp_params(Exp_y_Col_Index)),Exp_y_Col_Name)
                Cmp_Filename   = [cmpdir,inst{n},'/',strtrim(char(Cmp_params(Cmp_Filename_Col)))];
                Cmp_x_Col_Name = strtrim(char(Cmp_params(find(strcmp(strtrim(Cmp_headers{n}),'Cmp_x_Col_Name')))));
                Cmp_y_Col_Name = strtrim(char(Cmp_params(find(strcmp(strtrim(Cmp_headers{n}),'Cmp_y_Col_Name')))));
                Cmp_Plot_Style = strtrim(char(Cmp_params(find(strcmp(strtrim(Cmp_headers{n}),'Plot_Style')))));
                if exist(Cmp_Filename)
                    C = importdata(Cmp_Filename,',',1);
                    X2 = C.data(:,find(strcmp(strtrim(C.colheaders),Cmp_x_Col_Name)));
                    Y2 = C.data(:,find(strcmp(strtrim(C.colheaders),Cmp_y_Col_Name)));

                    n_key=n_key+1;
                    H(n_key)=plot(X2,Y2,Cmp_Plot_Style,'MarkerSize',Marker_Size);
                    Legend_Key{n_key} = inst{n};
                end
            end
        end

    end

    % do some plot formatting

    axis([xMin xMax yMin yMax])
    set(gca,'YTick',yMin:yTick:yMax)
    set(gca,'YMinorTick','on')
    set(gca,'XTick',xMin:xTick:xMax)
    set(gca,'XMinorTick','on')
    set(gca,'FontSize',Font_Size)
    xlabel(xLabel,'FontSize',Font_Size)
    ylabel(yLabel,'FontSize',Font_Size)
    lh=legend(H,Legend_Key,'Location',Legend_Location);
    set(lh,'FontSize',Font_Size)
    legend 'boxon'

    xt = xMin + .05*(xMax-xMin);
    yt = yMin + .92*(yMax-yMin);
    text(xt,yt,Plot_Title,'FontSize',Font_Size)

    % print to vector output

    loose_inset
    print(gcf,'-dpdf',[pltdir,Plot_Filename])

    clear H Legend_Key
    hold off

end