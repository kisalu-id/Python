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
    label = gdb.get_label()





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
                        sheets = nest.get_sheets()

                    for sheet in sheets:
                        width = nest.get_sheet_property(sheet, nest.SheetProperties.WIDTH)               #_NSheetWidth
                        height = nest.get_sheet_property(sheet, nest.SheetProperties.HEIGHT)             #_NSheetHeight
                        thickness = nest.get_sheet_property(sheet, nest.Properties.SHEET_THICKNESS)      #_NSheetRateReusable
                        matherial = nest.get_sheet_property(sheet, nest.SheetProperties.MATERIAL)        #_NSheetMaterial
                        name = gdb.get_names(part+'\\%%NESTDATA\\Pieces') #??
                        #ChangeLabelIntoId( sSheet) ;  #?????????????? how
                        if width > width:
                            if not rotate:
                                width_img = height * 0.35
                                height_img = height * 0.35
                            else:
                                width_img = width * 0.35
                                height_img = height * 0.35
                        else:
                            if not rotate:
                                width_img = height * 0.35
                                height_img = width * 0.35
                            else:
                                width_img = width * 0.35
                                height_img = height * 0.35
                        file = next(os.walk(folder))[2][0] if os.listdir(folder) else ""
                        object_path = sheet #???????????????????????????????????????????????
                        view.zoom_on_object(object_path, ratio=1)
                        # bOk = bOk  AND  ExportImage( sImgPath, nHeightImg, nWidthImg, 24) ;

                        # Tabelle aufmachen..
                        write_html()

                        #restore the initial sheet
                        #bOk = bOk  AND  NestActivateSheet( sCurrSheet) ;
                        if rotate:
                            cad.rotate(sheet, 0, 0, -90, False)
                        
                        # ProgressClose() ;
                        # SetShading() ;



def write_html():
    #open table
    line = "<TABLE"
    #start a new page
    if count != 0:
        line += ' style="page-break-before:always"'

    #table for customer information - header row
    line += f'> <TR> <TD rowspan="3"> <IMG src="{logo}" align="middle"> </TD> </TR>'
    line += '<TR> <TD> &nbsp; </TD> </TR>'
    line += f'<TR> <TD style="font-size:30px" align="right" width="150"> Projekt: </TD> <TD width="15"> &nbsp; </TD> <TD style="font-size:30px">{os.path.splitext(get_name())[0]}</TD> </TR> </TABLE>'
    file.write(line)

    # Table for sheet information
    line = '<TABLE border="1" cellspacing="1" cellpadding="1">'
    file.write(line)

    # Row with sheet name
    line = f'<TR> <TD style="font-size:30px" colspan="6" align="middle">{sheet}</TD>'

    count += 1
    s_count = str(count).zfill(3)
    #adding the barcode
    line += f'<TD id="code{s_count}" colspan="4" class="barcode">{sheet.upper()}</TD>'
    line += '</TR>'
    file.write(line)

    # Sheet information - Width, Height, Thickness, Name, Material
    line = f'<TR> <TD align="middle"> Breite </TD> <TD align="middle">{width}</TD>'
    line += f'<TD align="middle"> Höhe </TD> <TD align="middle">{height}</TD>'
    line += f'<TD align="middle"> Stärke </TD> <TD align="middle">{thickness}</TD>'
    line += f'<TD align="middle"> Name </TD> <TD align="middle">{name}</TD>'
    line += f'<TD align="middle"> Material </TD> <TD align="middle">{material}</TD></TR>'
    file.write(line)





    #picture from the sheet
    #sSizeImg = OPT( nWidth>3*nHeight, "width=^"1200pt^"", "height=^"400pt^"") ;
    size_img = "width=\"1200pt\"" if nWidth > 3 * nHeight else "height=\"400pt\""
    line = '<TR> <TD colspan="10"> <IMG src="file:///{img_path}"{size_img}> </TD></TR>'
    file.write(line)

    #Write down the individual information about the components.
    s_pieces = nest.get_pieces(sheet)
    n_piece_count = 1
    file = next(os.walk(folder))[2][0] if os.listdir(folder) else ""
    while (file != ""):
        line = "<TR> "
        #HTML Schnittplan
        line += f'<TD align="middle"> Nr. </TD> <TD align="middle">{n_piece_count}</TD>'

        label = nest.get_sheet_property(sheet, nest.Properties.PIECE_LABEL)
        width = nest.get_sheet_property(sheet, nest.SheetProperties.WIDTH)               #_NSheetWidth
        height = nest.get_sheet_property(sheet, nest.SheetProperties.HEIGHT)             #_NSheetHeight
        #bOk = bOk  AND  NestGetPieceProp( sPiece, _NPieceLabel, &sLabel) ;

        line += '<TD align="middle"> Bezeichnung </TD> <TD align="middle">{label}</TD>'
        line += '<TD align="middle"> Breite </TD> <TD align="middle">{width}</TD>'
        line += '<TD align="middle"> Breite </TD> <TD align="middle">{height}</TD>'
        line += '</TR>'
        file.write(line)
        n_piece_count += 1
        #close table
        line = '</TABLE></BR>'
        file.write(line)
        #update status

        perc = count / n_sheets
        #bOk = bOk  AND  ProgressUpdate( perc) ;   ????????
        count += 1

        insert_java_script()

        line = '</BODY></HTML>'
        file.write(line)
        #   bOk = bOk  AND  CloseFile( nFile) ;




if __name__ == '__main__':
    count_efficiency()
    make_report()
