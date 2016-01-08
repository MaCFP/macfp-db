% McDermott
% 08 Jan 2016
% sandia_flames.m

close all
clear all

expdir = '../Experimental_Data/';
cmpdir = '../Computational_Results/';
pltdir = '../Plots/';
addpath '../../../Utilities/'
plot_style

chid = cell(1,4);
chid{1} = {'Sandia_CH4_1m_Test14_p3','Sandia_CH4_1m_Test14_p5','Sandia_CH4_1m_Test14_p9'};
chid{2} = {'Sandia_CH4_1m_Test17_p3','Sandia_CH4_1m_Test17_p5','Sandia_CH4_1m_Test17_p9'};
chid{3} = {'Sandia_CH4_1m_Test24_p3','Sandia_CH4_1m_Test24_p5','Sandia_CH4_1m_Test24_p9'};
chid{4} = {'Sandia_H2_1m_Test35_p3','Sandia_H2_1m_Test35_p5','Sandia_H2_1m_Test35_p9'};

expxhdr = {'x (m)','x (m)','x (m)'};
expyhdr = {'U mean (m/s)','W mean (m/s)','TKE (m2/s2)'};
exp_marker_style = {'ro','bo','mo'};

title1 = {'Sandia 1 m Methane','Sandia 1 m Methane','Sandia 1 m Methane','Sandia 1 m Hydrogen'};
title2 = {'Test 14 (low flowrate)','Test 17 (high flowrate)','Test 24 (medium flowrate)','Test 35'};
title3 = {'z = 0.3 m','z = 0.5 m','z = 0.9 m'};
xlbl = {'x (m)','x (m)','x (m)'};
ylbl = {'Mean Radial Velocity (m/s)','Mean Vertical Velocity (m/s)','TKE (m2/s2)'};
pltid = {'_U','_W','_TKE'};

rel_error(1,:) =[.31,.20,.28]; % Test 14, see [Tieszen et al., 2004] 
rel_error(2,:) =[.45,.70,.78]; % Test 17
rel_error(3,:) =[.40,.45,.46]; % Test 24
rel_error(4,:) =[.55,.37,.40]; % Test 35

% format axis range and ticks

xmin = [-.5 -.5 -.5];  xmax = [ .5  .5  .5];   dx = [.1 .1 .1];
ymin = [-0.8 0 0];     ymax = [0.8 8 5];       dy = [.2 1 1];

data_stride = 4; % skip this number of points for readability

for k=1:length(chid) % k_for
    for i=1:length(chid{k}) % i_for

        % import experimental data

        E1 = importdata([expdir,chid{k}{i},'.csv'],',',1);

        x1 = E1.data(1:data_stride:end,find(strcmp(E1.colheaders,expxhdr{i})));

        for j=1:length(expyhdr) % j_for

            if (k==1 | k==2) & j==3 % skip TKE
                continue
            end

            figure; hold off

            y1 = E1.data(1:data_stride:end,find(strcmp(E1.colheaders,expyhdr{j})));
            plot(x1,y1,exp_marker_style{j},'MarkerSize',Marker_Size); hold on

            % add error bars

            e = rel_error(k,j)*abs(y1);
            H(1)=errorbar(x1,y1,-e,+e,exp_marker_style{j},'MarkerSize',Marker_Size);

            % plot computational results *********************************
            
            % add your results here!

            % ************************************************************

            xt = xmin(i) + .05*(xmax(i)-xmin(i));
            yt = ymin(j) + .92*(ymax(j)-ymin(j));
            text(xt,yt,title1{k},'FontSize',Font_Size)

            xt = xmin(i) + .05*(xmax(i)-xmin(i));
            yt = ymin(j) + .84*(ymax(j)-ymin(j));
            text(xt,yt,title2{k},'FontSize',Font_Size)

            xt = xmin(i) + .05*(xmax(i)-xmin(i));
            yt = ymin(j) + .76*(ymax(j)-ymin(j));
            text(xt,yt,title3{i},'FontSize',Font_Size)

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
            print(gcf,'-dpdf',[pltdir,chid{k}{i},pltid{j}])

        end % j_for

    end % i_for
end % k_for
