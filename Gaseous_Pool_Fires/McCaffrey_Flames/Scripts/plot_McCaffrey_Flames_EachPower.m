% McDermott
% 25 May 2017
% plot_McCaffrey_Flames.m

close all
clear all

restoredefaultpath
addpath '../../../Utilities/'

expdir = '../Experimental_Data/';
cmpdir = '../Computational_Results/2017/';
pltdir = '../Plots/';
plot_style

% read exp data configuration file
Exp = importdata([expdir,'McCaffrey_Flames_EachPower_dataplot_inputs.csv']);
Exp_H = textscan(Exp{1},'%q','delimiter',',');   % scan first line for line headers
Exp_headers = Exp_H{:}'; clear Exp_H             % store headers here
n_plots = length(Exp);

% get list of participants
inst = get_folder_list(cmpdir);
n_inst = length(inst);
% following loop from 1 to n_inst to include all institutions and data.
% Skip data as necessary (right now Data is the first in the list: inst{1}
for n = 1:n_inst
    Cmp{n} = importdata([cmpdir,inst{n},'/',inst{n},'_dataplot_inputs.csv']); % this file maps cmp data file to exp data file
    Cmp_H = textscan(Cmp{n}{1},'%q','delimiter',',');   % scan first line for line headers
    Cmp_headers{n} = Cmp_H{:}'; clear Cmp_H             % store headers here for each institution
end

for i=2:n_plots

    if i>n_plots; break; end

    % load experimental data for line {i} in McCaffrey_Flames_dataplot_inputs.csv

    P = textscan(Exp{i},'%q','delimiter',',');
    Exp_params = P{:}';   % These are the lines in correlation *_dataplot_inputs.csv below the header

    % Check to see if d line has been activated in configuration file
    %dtest = strcmp(Exp_params(strcmp(Exp_headers,'switch_id')),'d');

    %if dtest % dtest_if (else just skip line)

        Exp_Filename      = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Exp_Filename')))));
        Exp_x_Col_Name    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Exp_x_Col_Name')))));
        Exp_y_Col_Name    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Exp_y_Col_Name')))));
        Exp_Legend_Key    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Key_Label')))));
        Exp_Plot_Style    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Plot_Style')))));
        % This isn't in the *_dataplot_inputs.csv files.  Delineates
        % log-log, default loglog
        Exp_Plot_Type     = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Plot_Type')))));
        if size(Exp_Plot_Type)==0
            Exp_Plot_Type='loglog';
        end

        % We can set the legend location and the axis limits in the
        % *_dataplot_inputs.csv file if we add these columns.
        % OR we can hardcode them here
        xLabel            = strtrim(char(Exp_params(find(strcmp(Exp_headers,'xLabel')))));
        yLabel            = strtrim(char(Exp_params(find(strcmp(Exp_headers,'yLabel')))));
        xLabel            = Exp_x_Col_Name;
        yLabel            = Exp_y_Col_Name;
        xMin              = str2num(char(Exp_params(find(strcmp(Exp_headers,'xMin')))));
        xMax              = str2num(char(Exp_params(find(strcmp(Exp_headers,'xMax')))));
        yMin              = str2num(char(Exp_params(find(strcmp(Exp_headers,'yMin')))));
        yMax              = str2num(char(Exp_params(find(strcmp(Exp_headers,'yMax')))));
        xTick             = str2num(char(Exp_params(find(strcmp(Exp_headers,'xTick')))));
        yTick             = str2num(char(Exp_params(find(strcmp(Exp_headers,'yTick')))));
        Legend_Location   = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Legend_Location')))));
        Legend_Location   = 'NorthWest';
        if strfind(Exp_y_Col_Name,'dT')
            Plot_Filename   = sprintf('dT_%s',Exp_Legend_Key(end-4:end));
        elseif strfind(Exp_y_Col_Name,'V/Q')
            Plot_Filename   = sprintf('Vstar_%s',Exp_Legend_Key(end-4:end));
        end
        Plot_Title        = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Plot_Title')))));
        Plot_Title        = sprintf('%s %s',Exp_y_Col_Name,Exp_Legend_Key(end-4:end));
        E = importdata([expdir,Exp_Filename],',',1);

        X1 = E.data(:,find(strcmp(strtrim(E.colheaders),Exp_x_Col_Name)));
        Y1 = E.data(:,find(strcmp(strtrim(E.colheaders),Exp_y_Col_Name)));

        figure
        set(gca,'Units',Plot_Units)
        set(gca,'Position',[Plot_X Plot_Y Plot_Width Plot_Height])

        if strcmp(Exp_Plot_Type,'linear')
            H(1)=plot(X1,Y1,Exp_Plot_Style,'MarkerSize',Marker_Size,'LineWidth',Line_Width); hold on
        elseif strcmp(Exp_Plot_Type,'loglog')
            H(1)=loglog(X1,Y1,Exp_Plot_Style,'MarkerSize',Marker_Size,'LineWidth',Line_Width); hold on
        end
        n_key=1;
        Legend_Key{n_key} = Exp_Legend_Key;

        % load computational data from each institution
        %  skip the Data entry if desired
        for n=1:n_inst

            % % uncomment this if block to suppress data points or edit to only plot specific institutions
            % if strcmp(inst{n},'Data')
            %     continue
            % end

            % scan the Cmp list associated with Exp_Filename and Exp_y_Col_Name

            Exp_Filename_Col = find(strcmp(strtrim(Cmp_headers{n}),'Exp_Filename'));
            Cmp_Filename_Col = find(strcmp(strtrim(Cmp_headers{n}),'Cmp_Filename'));
            Exp_y_Col_Index  = find(strcmp(strtrim(Cmp_headers{n}),'Exp_y_Col_Name'));

            for k=2:length(Cmp{n})   % Here we go through the 11 lines of the  INST_dataplot_inputs.csv
                M = textscan(Cmp{n}{k},'%q','delimiter',',');
                Cmp_params = M{:}';
                % This first test matches the experimental file name listed
                % in the INST_dataplot_inputs.csv
                % The second test matches the y-variable name
                % ("dT (C)" or "V/Q^0.2")
                % The third item matches the power in the Exp data set
                Cmp_Key_Label  = strtrim(char(Cmp_params(find(strcmp(strtrim(Cmp_headers{n}),'Key_Label')))));
                if strcmp(strtrim(Cmp_params(Exp_Filename_Col)),Exp_Filename) & strcmp(strtrim(Cmp_params(Exp_y_Col_Index)),Exp_y_Col_Name) & strfind(Cmp_Key_Label,Exp_Legend_Key(end-4:end))
                    Cmp_Filename   = [cmpdir,inst{n},'/',strtrim(char(Cmp_params(Cmp_Filename_Col)))];
                    Cmp_x_Col_Name = strtrim(char(Cmp_params(find(strcmp(strtrim(Cmp_headers{n}),'Cmp_x_Col_Name')))));
                    Cmp_y_Col_Name = strtrim(char(Cmp_params(find(strcmp(strtrim(Cmp_headers{n}),'Cmp_y_Col_Name')))));
                    Cmp_Plot_Style = strtrim(char(Cmp_params(find(strcmp(strtrim(Cmp_headers{n}),'Plot_Style')))));
                    Cmp_Key_Label  = strtrim(char(Cmp_params(find(strcmp(strtrim(Cmp_headers{n}),'Key_Label')))));
                    Cmp_Header_Row = str2num(char(Cmp_params(find(strcmp(strtrim(Cmp_headers{n}),'Cmp_Header_Row')))));
                    if size(Cmp_Header_Row)==0
                        Cmp_Header_Row=1;
                    end
                    x_Scale = str2num(char(Cmp_params(find(strcmp(strtrim(Cmp_headers{n}),'x_Scale')))));
                    if size(x_Scale)==0
                        x_Scale=1;
                    end
                    y_Scale = str2num(char(Cmp_params(find(strcmp(strtrim(Cmp_headers{n}),'y_Scale')))));
                    if size(y_Scale)==0
                        y_Scale=1;
                    end
                    if exist(Cmp_Filename)
                        C = importdata(Cmp_Filename,',',Cmp_Header_Row);
                        X2 = x_Scale.*C.data(:,find(strcmp(strtrim(C.colheaders),Cmp_x_Col_Name)));
                        Y2 = y_Scale.*C.data(:,find(strcmp(strtrim(C.colheaders),Cmp_y_Col_Name)));

                        n_key=n_key+1;

                        if strcmp(Exp_Plot_Type,'linear')
                            H(n_key)=plot(X2,Y2,Cmp_Plot_Style,'MarkerSize',Marker_Size,'LineWidth',Line_Width)
                        elseif strcmp(Exp_Plot_Type,'loglog')
                            H(n_key)=loglog(X2,Y2,Cmp_Plot_Style,'MarkerSize',Marker_Size,'LineWidth',Line_Width);
                        end

                        if size(Cmp_Key_Label)==0
                            Legend_Key{n_key} = inst{n};
                        else
                            Legend_Key{n_key} = Cmp_Key_Label;
                        end
                    end

                end
            end

        end

        % do some plot formatting

        if size(xMin)>0 & size(xMax)>0 & size(yMin)>0 & size(yMax)>0
            axis([xMin xMax yMin yMax])
            if strcmp(Exp_Plot_Type,'linear')
                set(gca,'YTick',yMin:yTick:yMax)
                set(gca,'YMinorTick','on')
                set(gca,'XTick',xMin:xTick:xMax)
                set(gca,'XMinorTick','on')
            end
        else
            Pos = get(gca,'Position');
            xMin = Pos(1);
            xMax = Pos(1)+Pos(3);
            yMin = Pos(2);
            yMax = Pos(2)+Pos(4);
        end

        Title_Position = [0.05 0.92];
        if strcmp(Exp_Plot_Type,'loglog')
            xt = 10^(log10(xMin)+Title_Position(1)*(log10(xMax)-log10(xMin)));
            yt = 10^(log10(yMin)+Title_Position(2)*(log10(yMax)-log10(yMin)));
        else
            xt = xMin + Title_Position(1)*(xMax-xMin);
            yt = yMin + Title_Position(2)*(yMax-yMin);
        end
        text(xt,yt,Plot_Title,'FontSize',Font_Size)

        set(gca,'FontSize',Font_Size)
        xlabel(xLabel,'FontSize',Font_Size)
        ylabel(yLabel,'FontSize',Font_Size)
        lh=legend(H,Legend_Key,'Location',Legend_Location);
        set(lh,'FontSize',Font_Size)
        legend 'boxon'

        % print to vector output

        set(gcf,'Visible',Figure_Visibility);
        set(gcf,'Units',Paper_Units);
        set(gcf,'PaperSize',[Paper_Width Paper_Height]);
        set(gcf,'Position',[0 0 Paper_Width Paper_Height]);
        print(gcf,'-dpdf',[pltdir,Plot_Filename])

        clear H Legend_Key

    %end % dtest_if

end