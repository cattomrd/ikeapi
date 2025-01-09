from compare_files import compare_files

stado_list = compare_files(file1="../files_temp/lista.txt", file2="../listas_sync/lista.txt")
stado_listm3u = compare_files(file1="../files_temp/lista.m3u", file2="../listas_sync/lista.m3u")

match stado_list:
    case True:
        print("True")
    case False:
        print("False")
    case _:
        print("no existe")
