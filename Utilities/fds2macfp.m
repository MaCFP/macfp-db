% McDermott
% 5-3-2017
% fds2macfp.m
%
% This script takes the FDS line output files and converts them to
% two column X Y csv files.
%
% Files must be in current directory.  Inputs must be character strings.
%
% Example:
%
% >> fds2macfp('Sandia_CH4_1m_Test14_dx1p5cm_line.csv','x','Up5','NIST_Sandia_CH4_1m_Test14_U_p5.csv','x (m)','U mean (m/s)')
%
% Inputs for fds_ylabel can be a cell array and you can add the argument
% 'TKE' to generate TKE from columns of RMS data.
%
% Example:
%
% >> fds2macfp('Sandia_CH4_1m_Test24_dx1p5cm_line.csv','x',{'Up3_rms','Wp3_rms'},'NIST_Sandia_CH4_1m_Test14_TKE_p3.csv','x (m)','TKE (m2/s2)','TKE')

function [] = fds2macfp(fds_file,fds_xlabel,fds_ylabel,macfp_file,macfp_xlabel,macfp_ylabel,varargin)

nArgs = length(varargin);

if nArgs==0
    M = importdata([pwd,'/',fds_file],',',2);
    xCol_Index = find(strcmp(M.colheaders,fds_xlabel));
    yCol_Index = find(strcmp(M.colheaders,fds_ylabel));
    X = M.data(:,xCol_Index);
    Y = M.data(:,yCol_Index);

    fid = fopen([pwd,'/',macfp_file],'wt');
    fprintf(fid,'%s, %s\n',macfp_xlabel,macfp_ylabel);
    for i=1:length(X)
        fprintf(fid,'%f, %f\n',X(i),Y(i));
    end
    fclose(fid);
else
    switch char(varargin)
        case {'TKE'}
            M = importdata([pwd,'/',fds_file],',',2);
            xCol_Index = find(strcmp(M.colheaders,fds_xlabel));
            yCol_Index_1 = find(strcmp(M.colheaders,fds_ylabel{1}));
            yCol_Index_2 = find(strcmp(M.colheaders,fds_ylabel{2}));
            X = M.data(:,xCol_Index);
            Y1 = M.data(:,yCol_Index_1);
            Y2 = M.data(:,yCol_Index_2);
            TKE = 0.5*(Y1.^2 + Y2.^2);

            fid = fopen([pwd,'/',macfp_file],'wt');
            fprintf(fid,'%s, %s\n',macfp_xlabel,macfp_ylabel);
            for i=1:length(X)
                fprintf(fid,'%f, %f\n',X(i),TKE(i));
            end
            fclose(fid);
    end
end