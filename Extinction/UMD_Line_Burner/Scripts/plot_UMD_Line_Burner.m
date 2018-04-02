% McDermott
% 25 May 2017
% plot_UMD_Line_Burner.m

close all
clear all

restoredefaultpath
addpath '../../../Utilities/'

expdir = '../Experimental_Data/';
cmpdir = '../Computational_Results/2017/';
pltdir = '/Volumes/rmcdermo/tmp_plots/';
plot_style

% read exp data configuration file
Exp = importdata([expdir,'UMD_Line_Burner_dataplot_inputs.csv']);
Exp_H = textscan(Exp{1},'%q','delimiter',',');
Exp_headers = Exp_H{:}'; clear Exp_H
n_plots = length(Exp);

% get list of participants
inst = get_folder_list(cmpdir);
n_inst = length(inst);
for n = 1:n_inst
    Cmp_inputs_exist(n) = 0;
    if exist([cmpdir,inst{n},'/',inst{n},'_dataplot_inputs.csv'])
        Cmp_inputs_exist(n) = 1;
        Cmp{n} = importdata([cmpdir,inst{n},'/',inst{n},'_dataplot_inputs.csv']); % this file maps cmp data file to exp data file
        Cmp_H = textscan(Cmp{n}{1},'%q','delimiter',',');
        Cmp_headers{n} = Cmp_H{:}'; clear Cmp_H
    end
end

for i=2:n_plots

    if i>n_plots; break; end

    % load experimental data

    P = textscan(Exp{i},'%q','delimiter',',');
    Exp_params = P{:}';

    % Check to see if d line has been activated in configuration file
    dtest = strcmp(Exp_params(strcmp(Exp_headers,'switch_id')),'d');

    if dtest % dtest_if (else just skip line)

        Exp_Filename      = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Data_Filename')))));
        Exp_x_Col_Name    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'x_Col_Name')))));
        Exp_y_Col_Name    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'y_Col_Name')))));
        Exp_Legend_Key    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Legend_Key')))));
        Exp_Plot_Style    = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Plot_Style')))));
        Exp_Plot_Type     = strtrim(char(Exp_params(find(strcmp(Exp_headers,'Plot_Type')))));
        if size(Exp_Plot_Type)==0
            Exp_Plot_Type='linear';
        end

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
        Plot_Title        = ''; %strtrim(char(Exp_params(find(strcmp(Exp_headers,'Plot_Title')))));

        E = importdata([expdir,Exp_Filename],',',1);

        X1 = E.data(:,find(strcmp(strtrim(E.colheaders),Exp_x_Col_Name)));
        Y1 = E.data(:,find(strcmp(strtrim(E.colheaders),Exp_y_Col_Name)));

        figure
        set(gca,'Units',Plot_Units)
        set(gca,'Position',[Plot_X Plot_Y Plot_Width Plot_Height])

        if strcmp(Exp_Plot_Type,'linear')
            % H(1)=plot(X1,Y1,Exp_Plot_Style,'LineWidth',Line_Width,'MarkerSize',Marker_Size); hold on
            Marker_Size = 10;
            Marker_Edge_Color = 'k';
            Marker_Face_Color = 'k';
            H(1)=plot(X1,Y1,Exp_Plot_Style,'MarkerSize',Marker_Size, ...
               'MarkerEdgeColor',Marker_Edge_Color, ...
               'MarkerFaceColor',Marker_Face_Color);
            hold on
        elseif strcmp(Exp_Plot_Type,'loglog')
            H(1)=loglog(X1,Y1,Exp_Plot_Style,'LineWidth',Line_Width,'MarkerSize',Marker_Size); hold on
        end
        n_key=1;
        Legend_Key{n_key} = Exp_Legend_Key;

        % load computational data from each institution

        for n=1:n_inst

            % % uncomment this if block to suppress data points or edit to only plot specific institutions
            % if strcmp(inst{n},'Data')
            %     continue
            % end

            % scan the Cmp list associated with Exp_Filename and Exp_y_Col_Name

            if ~Cmp_inputs_exist(n)
                continue
            end

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
                            % H(n_key)=plot(X2,Y2,Cmp_Plot_Style,'LineWidth',Line_Width,'MarkerSize',Marker_Size);
                            if(n_key==2)
                               Line_Width  = 4;
                               Color = 'k';
                               Cmp_Plot_Style = '-';
                            elseif(n_key==3)
                               Line_Width  = 4;
                               Color = 'r';
                               Cmp_Plot_Style = '--';
                            elseif(n_key==4)
                               Line_Width  = 4;
                               Color = 'b';
                               Cmp_Plot_Style = '-.';
                            elseif(n_key==5)
                               Line_Width  = 4;
                               Color = [0.5 0 0.5];
                               Cmp_Plot_Style = ':';
                            elseif(n_key==6)
                               Line_Width  = 4;
                               Color = [0 0.5 0];
                               Cmp_Plot_Style = ':';
                            end
                            H(n_key)=plot(X2,Y2,Cmp_Plot_Style,'LineWidth',Line_Width,'Color',Color);
                        elseif strcmp(Exp_Plot_Type,'loglog')
                            H(n_key)=loglog(X2,Y2,Cmp_Plot_Style,'LineWidth',Line_Width,'MarkerSize',Marker_Size);
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
        % lh=legend(H,Legend_Key,'Location',Legend_Location);
        % set(lh,'FontSize',Font_Size)
        % legend 'boxon'

        % print to vector output

        set(gcf,'Visible',Figure_Visibility);
        set(gcf,'Units',Paper_Units);
        set(gcf,'PaperSize',[Paper_Width Paper_Height]);
        set(gcf,'Position',[0 0 Paper_Width Paper_Height]);
        print(gcf,'-dpdf',[pltdir,Plot_Filename])

        clear H Legend_Key

    end % dtest_if

end