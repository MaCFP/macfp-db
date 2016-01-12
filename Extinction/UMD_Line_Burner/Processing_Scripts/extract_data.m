% McDermott
% 1-12-2016
% extract_data.m

close all
clear all

expdir = '../Experimental_Data/';

D = load([expdir,'Data.mat'])

% extract TC data

M(:,1) = D.TC_Data.x_125;
M(:,2) = D.TC_Data.x_250;
M(:,3) = D.TC_Data.TC_125;
M(:,4) = D.TC_Data.TC_250;

header = {'x_125','x_250','TC_125','TC_250'};
filename = [expdir,'TC_Data.csv'];
fid = fopen(filename,'wt');
fprintf(fid,'%s,',header{1:(end-1)}); fprintf(fid,'%s',header{end}); fprintf(fid,'\n');
for i=1:length(M(:,1))
    fprintf(fid,'%f,',M(i,1:(end-1))); fprintf(fid,'%f',M(i,end)); fprintf(fid,'\n');
end
fclose(fid);

% extract O2 data

clear M
M(:,1) = D.O2_Data.x_125;
M(:,2) = D.O2_Data.x_250;
M(:,3) = D.O2_Data.XO2_125;
M(:,4) = D.O2_Data.XO2_250;

header = {'x_125','x_250','XO2_125','XO2_250'};
filename = [expdir,'O2_Data.csv'];
fid = fopen(filename,'wt');
fprintf(fid,'%s,',header{1:(end-1)}); fprintf(fid,'%s',header{end}); fprintf(fid,'\n');
for i=1:length(M(:,1))
    fprintf(fid,'%f,',M(i,1:(end-1))); fprintf(fid,'%f',M(i,end)); fprintf(fid,'\n');
end
fclose(fid);

% propane anchored data vs. XO2

clear M
M(:,1) = D.C3H8_A.XO2;
M(:,2) = D.C3H8_A.Chi_R;
M(:,3) = D.C3H8_A.q_R;
M(:,4) = D.C3H8_A.Q_f;
M(:,5) = D.C3H8_A.Q_O2;
M(:,6) = D.C3H8_A.Q_CO2;
M(:,7) = D.C3H8_A.eta;
M(:,8) = D.C3H8_A.S_XO2;
M(:,9) = D.C3H8_A.S_ChiR;
M(:,10) = D.C3H8_A.S_qR;
M(:,11) = D.C3H8_A.S_Qf;
M(:,12) = D.C3H8_A.S_QO2;
M(:,13) = D.C3H8_A.S_QCO2;
M(:,14) = D.C3H8_A.S_eta;

header = {'XO2','Chi_R','q_R','Q_f','Q_O2','Q_CO2','eta','S_XO2','S_ChiR','S_qR','S_Qf','S_QO2','S_QCO2','S_eta'};
filename = [expdir,'C3H8_A_Data.csv'];

fid = fopen(filename,'wt');
fprintf(fid,'%s,',header{1:(end-1)}); fprintf(fid,'%s',header{end}); fprintf(fid,'\n');
for i=1:length(M(:,1))
    fprintf(fid,'%f,',M(i,1:(end-1))); fprintf(fid,'%f',M(i,end)); fprintf(fid,'\n');
end
fclose(fid);

% propane anchored flame height data

clear M
M(:,1) = D.C3H8_A.Lf;
M(:,2) = D.C3H8_A.S_Lf;
M(:,3) = D.C3H8_A.XO2_Lf;

header = {'Lf','XO2_Lf'};
filename = [expdir,'C3H8_A_Lf_Data.csv'];

fid = fopen(filename,'wt');
fprintf(fid,'%s,',header{1:(end-1)}); fprintf(fid,'%s',header{end}); fprintf(fid,'\n');
for i=1:length(M(:,1))
    fprintf(fid,'%f,',M(i,1:(end-1))); fprintf(fid,'%f',M(i,end)); fprintf(fid,'\n');
end
fclose(fid);

% propane non-anchored data vs. XO2

clear M
M(:,1) = D.C3H8_NA.XO2;
M(:,2) = D.C3H8_NA.Chi_R;
M(:,3) = D.C3H8_NA.q_R;
M(:,4) = D.C3H8_NA.Q_f;
M(:,5) = D.C3H8_NA.Q_O2;
M(:,6) = D.C3H8_NA.Q_CO2;
M(:,7) = D.C3H8_NA.eta;
M(:,8) = D.C3H8_NA.S_XO2;
M(:,9) = D.C3H8_NA.S_ChiR;
M(:,10) = D.C3H8_NA.S_qR;
M(:,11) = D.C3H8_NA.S_Qf;
M(:,12) = D.C3H8_NA.S_QO2;
M(:,13) = D.C3H8_NA.S_QCO2;
M(:,14) = D.C3H8_NA.S_eta;

header = {'XO2','Chi_R','q_R','Q_f','Q_O2','Q_CO2','eta','S_XO2','S_ChiR','S_qR','S_Qf','S_QO2','S_QCO2','S_eta'};
filename = [expdir,'C3H8_NA_Data.csv'];

fid = fopen(filename,'wt');
fprintf(fid,'%s,',header{1:(end-1)}); fprintf(fid,'%s',header{end}); fprintf(fid,'\n');
for i=1:length(M(:,1))
    fprintf(fid,'%f,',M(i,1:(end-1))); fprintf(fid,'%f',M(i,end)); fprintf(fid,'\n');
end
fclose(fid);

% propane anchored flame height data

clear M
M(:,1) = D.C3H8_NA.Lf;
M(:,2) = D.C3H8_NA.S_Lf;
M(:,3) = D.C3H8_NA.XO2_Lf;

header = {'Lf','XO2_Lf'};
filename = [expdir,'C3H8_NA_Lf_Data.csv'];

fid = fopen(filename,'wt');
fprintf(fid,'%s,',header{1:(end-1)}); fprintf(fid,'%s',header{end}); fprintf(fid,'\n');
for i=1:length(M(:,1))
    fprintf(fid,'%f,',M(i,1:(end-1))); fprintf(fid,'%f',M(i,end)); fprintf(fid,'\n');
end
fclose(fid);

% methane anchored data vs. XO2

clear M
M(:,1) = D.CH4_A.XO2;
M(:,2) = D.CH4_A.Chi_R;
M(:,3) = D.CH4_A.q_R;
M(:,4) = D.CH4_A.Q_f;
M(:,5) = D.CH4_A.Q_O2;
M(:,6) = D.CH4_A.Q_CO2;
M(:,7) = D.CH4_A.eta;
M(:,8) = D.CH4_A.S_XO2;
M(:,9) = D.CH4_A.S_ChiR;
M(:,10) = D.CH4_A.S_qR;
M(:,11) = D.CH4_A.S_Qf;
M(:,12) = D.CH4_A.S_QO2;
M(:,13) = D.CH4_A.S_QCO2;
M(:,14) = D.CH4_A.S_eta;

header = {'XO2','Chi_R','q_R','Q_f','Q_O2','Q_CO2','eta','S_XO2','S_ChiR','S_qR','S_Qf','S_QO2','S_QCO2','S_eta'};
filename = [expdir,'CH4_A_Data.csv'];

fid = fopen(filename,'wt');
fprintf(fid,'%s,',header{1:(end-1)}); fprintf(fid,'%s',header{end}); fprintf(fid,'\n');
for i=1:length(M(:,1))
    fprintf(fid,'%f,',M(i,1:(end-1))); fprintf(fid,'%f',M(i,end)); fprintf(fid,'\n');
end
fclose(fid);

% propane anchored flame height data

clear M
M(:,1) = D.CH4_A.Lf;
M(:,2) = D.CH4_A.S_Lf;
M(:,3) = D.CH4_A.XO2_Lf;

header = {'Lf','XO2_Lf'};
filename = [expdir,'CH4_A_Lf_Data.csv'];

fid = fopen(filename,'wt');
fprintf(fid,'%s,',header{1:(end-1)}); fprintf(fid,'%s',header{end}); fprintf(fid,'\n');
for i=1:length(M(:,1))
    fprintf(fid,'%f,',M(i,1:(end-1))); fprintf(fid,'%f',M(i,end)); fprintf(fid,'\n');
end
fclose(fid);

% methane non-anchored data vs. XO2

clear M
M(:,1) = D.CH4_NA.XO2;
M(:,2) = D.CH4_NA.Chi_R;
M(:,3) = D.CH4_NA.q_R;
M(:,4) = D.CH4_NA.Q_f;
M(:,5) = D.CH4_NA.Q_O2;
M(:,6) = D.CH4_NA.Q_CO2;
M(:,7) = D.CH4_NA.eta;
M(:,8) = D.CH4_NA.S_XO2;
M(:,9) = D.CH4_NA.S_ChiR;
M(:,10) = D.CH4_NA.S_qR;
M(:,11) = D.CH4_NA.S_Qf;
M(:,12) = D.CH4_NA.S_QO2;
M(:,13) = D.CH4_NA.S_QCO2;
M(:,14) = D.CH4_NA.S_eta;

header = {'XO2','Chi_R','q_R','Q_f','Q_O2','Q_CO2','eta','S_XO2','S_ChiR','S_qR','S_Qf','S_QO2','S_QCO2','S_eta'};
filename = [expdir,'CH4_NA_Data.csv'];

fid = fopen(filename,'wt');
fprintf(fid,'%s,',header{1:(end-1)}); fprintf(fid,'%s',header{end}); fprintf(fid,'\n');
for i=1:length(M(:,1))
    fprintf(fid,'%f,',M(i,1:(end-1))); fprintf(fid,'%f',M(i,end)); fprintf(fid,'\n');
end
fclose(fid);

% propane anchored flame height data

clear M
M(:,1) = D.CH4_NA.Lf;
M(:,2) = D.CH4_NA.S_Lf;
M(:,3) = D.CH4_NA.XO2_Lf;

header = {'Lf','XO2_Lf'};
filename = [expdir,'CH4_NA_Lf_Data.csv'];

fid = fopen(filename,'wt');
fprintf(fid,'%s,',header{1:(end-1)}); fprintf(fid,'%s',header{end}); fprintf(fid,'\n');
for i=1:length(M(:,1))
    fprintf(fid,'%f,',M(i,1:(end-1))); fprintf(fid,'%f',M(i,end)); fprintf(fid,'\n');
end
fclose(fid);

