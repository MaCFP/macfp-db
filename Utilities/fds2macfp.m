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
% >> fds2macfp('Sandia_CH4_1m_Test14_dx1p5cm_line.csv','x','Up5','NIST_Sandia_CH4_1m_Test14_Up5.csv','x (m)','U mean (m/s)')

function [] = fds2macfp(fds_file,fds_xlabel,fds_ylabel,macfp_file,macfp_xlabel,macfp_ylabel)

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