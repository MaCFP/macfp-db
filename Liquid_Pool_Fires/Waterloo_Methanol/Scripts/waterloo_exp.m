% McDermott
% 5-18-2017
% waterloo_exp.m
%
% This script was used to reshape the original experimental data files.

close all
clear all

filename = '../Experimental_Data/Estimated_correlations';
M = importdata([filename,'.csv'],',',1);
M.colheaders{1} = 'z (cm)';
M.colheaders{2} = 'r (cm)';

z = [2,4,6,8,10,12,14,16,18,20,30];

for i=1:length(z)

    fid = fopen([filename,'_z',num2str(z(i)),'cm.csv'],'wt');

    ns = ['%s'];
    ng = ['%g'];
    for j=2:length(M.colheaders)
        ns = [ns,',%s'];
        ng = [ng,',%g'];
    end

    fprintf(fid,[ns,'\n'],M.colheaders{:});

    jrows = find(M.data(:,find(strcmp(M.colheaders,'z (cm)')))==z(i));

    for j=1:length(jrows)
        fprintf(fid,[ng,'\n'],M.data(jrows(j),:));
    end

    fclose(fid);

end

