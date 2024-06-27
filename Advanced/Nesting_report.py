from company import dlg
from sclcore import do_debug
from config import run_config



def count_efficiency():
    do_debug()
    nFileReport = r'C:\Users\...\Nesting_report\outlog.txt'


    nest.activate()
    nest_get_sheets = nest.get_sheets()

    if nest_get_sheets:
        with open(nFileReport, 'w') as file:
            nC = 1
            total_area = 0
            total_left = 0
            total_garbage = 0
            total_reusable = 0
            nSheets = 0
            for sheet in nest_get_sheets:
                area = nest.get_sheet_property(sheet, nest.SheetProperties.AREA)                 #_NSheetArea
                matherial = nest.get_sheet_property(sheet, nest.SheetProperties.MATERIAL)        #_NSheetMaterial
                width = nest.get_sheet_property(sheet, nest.SheetProperties.WIDTH)               #_NSheetWidth
                height = nest.get_sheet_property(sheet, nest.SheetProperties.HEIGHT)             #_NSheetHeight
                pieces = nest.get_sheet_property(sheet, nest.SheetProperties.PIECES_NUMBER)      #_NSheetNumPieces
                curr1 = nest.get_sheet_property(sheet, nest.SheetProperties.RATE_LEFT_OVER)      #_NSheetRateLeftOver  % of sheet   garbage not reusable material
                curr2 = nest.get_sheet_property(sheet, nest.SheetProperties.RATE_REUSABLE)       #_NSheetRateReusable  % of sheet   reusable material
                area = (area / 1000000) # m2
                total_area += area      # m2
                total_garbage += curr1  # %
                total_reusable += curr2 # %
                sC = str(nC).zfill(3)
                nSheets += 1
                nC += 1

                line_stats = f"Sheet{sC} - Material : {matherial}, Länge : {(width / 1000)}m, Breite : {(height / 1000)}m, Guteile : {pieces}\n"
                file.write(line_stats)

                line_eff = f"Effizienz von Sheet{sC}:\n  Fläche:  {round(area, 2)} m²,\n  Nicht wiederverwendbares Material:  {round(curr1, 2)}% des Blattes,\n  Wiederverwendbares Material:        {round(curr2, 2)}% des Blattes\n\n"
                
                file.write(line_eff)

            total_garbage /= nSheets #bc I need to not only add % from every sheet but also get the Durchschnitt
            total_reusable /= nSheets
            file.write(f"\nAnzahl Sheets :  {nSheets}\n")
            file.write(f"Gesamtfläche:  {round(total_area, 2)} m²\n\n")
            file.write(f"Wiederverwendbares Material pro Blatt im Durchschnitt:        {round(total_area * total_reusable / 100, 2)} m²\n")
            file.write(f"Nicht wiederverwendbares Material pro Blatt im Durchschnitt:  {round(total_area * total_garbage / 100, 2)} m²\n\n")
            file.write(f"Wiederverwendbares Material pro Blatt im Durchschnitt:        {round(total_reusable, 2)}%\n")
            file.write(f"Nicht wiederverwendbares Material pro Blatt im Durchschnitt:  {round(total_garbage, 2)}%\n\n")






















def change_label_into_id(s_sheet):
    gdb.get_label(lay)
    gdb.set_label()





def insert_java_script(file, nCount):
    file.write("<script type=^\"text/javascript^\">")
    file.write("/* <![CDATA[ */")
    file.write("function get_object(id) {")
    file.write("    var object = null;")
    file.write("    if (document.layers) {")
    file.write("        object = document.layers[id];")
    file.write("    } else if (document.all) {")
    file.write("        object = document.all[id];")
    file.write("    } else if (document.getElementById) {")
    file.write("        object = document.getElementById(id);")
    file.write("    }")
    file.write("    return object;")
    file.write("}")

    while(nCount > 0):
        sCount = str(nCount).zfill(3)
        sInt = (f'get_object("code{sCount}").innerHTML = DrawHTMLBarcode_Code39(get_object("code{sCount}").innerHTML, 0, "yes", "in", 0, 3, 0.4, 3, "top", "center", "", "black", "white");')
        file.write(sInt)
        nCount -= 1

    file.write("/* ]]> */")
    file.write("</script>")







def make_report():
    nFileReport = r'C:\Users\...\Nesting_report\report.html
    # cfg_file = open(ewd.explode_file_path(INI_PATH), 'w')
    with open(nFileReport, 'w') as file:
        s_sheets = nest.get_sheets()
        # if project is only saved, then the scl is aborted
        #   if( $NLS) return ;
        #   dodebug() ;
        # if file is not saved, then abort here...
        # if( STRSTR( GetName(), ".ewd") < 1) {
        if not file.endswith (".ewd"):
            dlg.output_box( "Projekt bitte speichern... \n Die Schnittpläne & Labels wurden nicht erstellt.")
        
        #path for the print files
        # = ExplodeFilePath( "%SETTINGPATH%" + "\Nest\Print") ;  
        folder = r'%MACHPATH%\\Nest\Print' #--- need to do something better than this

        if not folder: #if folder doesn't exist, crate
            os.makedirs(folder, exist_ok=False)
        #except FileExistsError:
        else:
        #// if available, these will be deleted first
            file = next(os.walk(folder))[2][0] if os.listdir(folder) else ""
            while (file != ""):
                    os.remove(os.path.join(folder, file))
                    file = next(os.walk(folder))[2][0] if os.listdir(folder) else ""


        ok = True
        n_sheets = 0
        folder = (f"{folder}\\")
        img_ext = ".jpg"
        img_path = r'C:\Users\...\Nesting_report\logo1.png
        #(ewd.explode_file_path(img_path), 'w')
        logo   = (f"file:///{img_path}") #URL


        # auf Draufsicht wechseln...und drahtgitter
        #Ok = bOk  AND  SetStdViewEye( 1)
        view.set_std_view_eye()
        #Ok = bOk  AND  SetWireFrame() ???????????????

        # 3 Dateien öffnen...
        # HTML Schnittplan
        out_file_path = (f"{folder}index.html")
        #try: except later
        with open(out_file_path, 'w') as out_file:
            # Öffnet Statuszeile
            #Ok = bOk  AND  ProgressCreate( "Print") ;

            # HTML Header und Datei Name
            file.write("<!doctype html>\n")
            file.write("<html lang=\"de\">\n")
            file.write("<meta charset=\"UTF-8\">\n")
            file.write(f"<head><title>{get_name()}</title>\n")
            file.write("<script type=\"text/javascript\" src=\"js/code39.js\"></script>\n")
            file.write("</head>\n")
            file.write("<body>\n")


            for sheet in s_sheets:
            # Sheets Liste aufrufen...
            # Anzahl Sheets und leere Sheets löschen...
                if sheet == "":
                    #NestDeleteSheets( sSheet)
                    sheet_to_delete = list(sheet)
                    nest.delete_sheets(sheet_to_delete) # ??? I'm very unsure what im doinggggggggg; I didn't find how to delete a sindle sheet
                else:
                    n_sheets += 1
                # Sheets um 90 Grad drehen...
                cad.rotate(sheet, 0, 0, -90, False)
                s_sheets = nest.get_sheets()
                n_count = 0
                file = next(os.walk(folder))[2][0] if os.listdir(folder) else ""
                    while (file != ""):
                        # Name of the jpg
                        #sImgPath = sFolder + sSheet + sImgExt ;   
                        nest.activate()






if __name__ == '__main__':
    count_efficiency()
    make_report()
