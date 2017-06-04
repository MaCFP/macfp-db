% return the directory folder list without hidden files or directories
function folder_list = get_folder_list(indir)
rehash
indir_list=dir(indir);
folder_list={};
jj=0;
for j=1:length(indir_list)
    if ~strcmp(indir_list(j).name(1),'.')
        jj=jj+1;
        folder_list{jj}=indir_list(j).name;
    end
end