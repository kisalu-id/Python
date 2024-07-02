import os
from datetime import datetime
import ewd
#import pdfkit #not working
from ewd import groups
from company import gdb
from company import dlg
from company import nest
from company.gdb import cad
from company.gdb import path
from company.gdb.view import redraw_window, zoom_all
from company.gdb import view
from config import run_config
from sclcore import do_debug


def change_label_into_id(s_sheet):
    #??? I don't know
    label = gdb.get_label()
    

def insert_java_script(file, nCount):
    line = f"""
    <script type="text/javascript">
    /* <![CDATA[ */
    function get_object(id) {{
        var object = null;
        if (document.layers) {{
            object = document.layers[id];
        }} else if (document.all) {{
            object = document.all[id];
        }} else if (document.getElementById) {{
            object = document.getElementById(id);
        }}
        return object;
    }}
    """
    file.write(line)

    while(nCount > 0):
        sCount = str(nCount).zfill(3)
        line = f'get_object("code{sCount}").innerHTML = DrawHTMLBarcode_Code39(get_object("code{sCount}").innerHTML, 0, "yes", "in", 0, 3, 0.4, 3, "top", "center", "", "black", "white");\n'
        file.write(line)
        nCount -= 1

    line = """
    /* ]]> */
    </script>
    """
    file.write(line)



def main():
    rotate = False #create hacken in settings or something like that

    do_debug()
    # if project is only saved, then the scl is aborted
    #   if( $NLS) return ;
    #   dodebug() ;
    # if file is not saved, then abort here...
    # if( STRSTR( GetName(), ".ewd") < 1) {
    project_name = ewd.get_project_name() # get the name of the opened ewd project
    if not project_name.endswith (".ewd"):
        dlg.output_box( "EWD Datei ewartet; Projekt bitte speichern. \nDie Schnittpläne & Labels wurden nicht erstellt.")
    
    #path for the print files
    # = ExplodeFilePath( "%SETTINGPATH%" + "\Nest\Print") ;  
    folder = r'C:\Users\...\Nesting_report\Nest\Print' #--- need to do something better than this

    #if folder doesn't exist, crate
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=False) #not sureeee
    
    # if available, these will be deleted first
    #iterate through each file and remove every file
    file_in_folder = next(os.walk(folder))[2][0] if os.listdir(folder) else ""
    while (file_in_folder != ""):
            os.remove(os.path.join(folder, file_in_folder))
            file_in_folder = next(os.walk(folder))[2][0] if os.listdir(folder) else ""

    report_file = r'C:\Users\...\Nest\Print\report.html'
    if not os.path.isfile(report_file):
        os.makedirs(os.path.dirname(report_file), exist_ok=True)

    ok = True
    n_sheets = 0
    if not folder.endswith("\\"):
        folder += "\\"
    img_ext = ".jpg"

    logo = (f"file:///{report_file}\\logo1.png") #URL

    #switch to top view; wireframe
    view.set_std_view_eye()
    #Ok = bOk  AND  SetWireFrame() ? how to make it

    #open 3 files
    #try: except, write later

    with open(report_file, 'w', encoding='utf-8') as html_file:
            #open status bar            Ok = bOk  AND  ProgressCreate( "Print") ;

            #if my program is working with 2 files at the same time (writing to html and getting info out of ewd) do i have to open-close them each time?? how does it work?
            #HTML header and file name
            html_file.write(html_header_write(project_name))
            nest.activate()
            sheets = nest.get_sheets()
            for sheet in sheets: #call sheets list, delete number of sheets and empty sheets
                if sheet == "": #how can it see that its empty or not?
                    sheet_to_delete = list(sheet) #NestDeleteSheets( sSheet)
                    #mb change modul???
                    nest.delete_sheets(sheet_to_delete) # ??? I'm very unsure what im doing; I didn't find how to delete a single sheet
                else:
                    n_sheets += 1

                if rotate: #rotate sheets by 90 degrees
                    cad.rotate(sheet, 0, 0, -90, False)

            sheets = nest.get_sheets()
            count = 0

            for sheet in sheets:
                #name of the jpg
                img_path = f"{folder}{sheet}{img_ext}"


                nC = 1
                total_area = 0
                total_garbage = 0
                total_reusable = 0
                nSheets = 0
                width = nest.get_sheet_property(sheet, nest.SheetProperties.WIDTH)               #_NSheetWidth
                height = nest.get_sheet_property(sheet, nest.SheetProperties.HEIGHT)             #_NSheetHeight
                thickness = nest.get_sheet_property(sheet, nest.Properties.SHEET_THICKNESS)      #_NSheetRateReusable
                material = nest.get_sheet_property(sheet, nest.SheetProperties.MATERIAL)         #_NSheetMaterial
                area = nest.get_sheet_property(sheet, nest.SheetProperties.AREA)                 #_NSheetArea
                pieces = nest.get_sheet_property(sheet, nest.SheetProperties.PIECES_NUMBER)      #_NSheetNumPieces
                curr1 = nest.get_sheet_property(sheet, nest.SheetProperties.RATE_LEFT_OVER)      #_NSheetRateLeftOver  % of sheet   garbage not reusable material
                curr2 = nest.get_sheet_property(sheet, nest.SheetProperties.RATE_REUSABLE)       #_NSheetRateReusable  % of sheet   reusable material
                area = (area / 1000000) # m2
                total_area += area      # m2
                total_garbage += curr1  # %
                total_reusable += curr2 # %

                name = sheet
                #ChangeLabelIntoId( sSheet) ;  #?????????????? how
                if width > height:
                    if not rotate:
                        width_img = height * 0.35
                        height_img = width * 0.35
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

                object_path = groups.get_current()
                #?  # cfg_file = open(ewd.explode_file_path(INI_PATH), 'w')
                #get_project_path

                if not os.path.isfile(img_path):
                    os.makedirs(os.path.dirname(img_path), exist_ok=True)

                view.zoom_on_object(object_path, ratio=1)
                nest.get_sheet_preview(sheet, img_path, 1.)
                # bOk = bOk  AND  ExportImage( sImgPath, nHeightImg, nWidthImg, 24) ;

                #html efficiency for each sheet
                write_html(html_file, logo, project_name, sheet, sheets, n_sheets, count, thickness, name, material, folder, pieces, total_area, curr1, curr2, total_reusable, total_garbage, img_path)
    
                nSheets += 1
                nC += 1

                #restore the initial sheet
                #bOk = bOk  AND  NestActivateSheet( sCurrSheet) ;

                if rotate:
                    cad.rotate(sheet, 0, 0, -90, False)
                
                # ProgressClose() ;    close progressbar 
                # SetShading() ;      Set the view as shaded

                #to_pdf()


def write_html(file, logo, project_name, sheet, sheets, n_sheets, count, thickness, name, material, folder, pieces, total_area, curr1, curr2, total_reusable, total_garbage, img_path):  ####maaaaybe do that differently
    #label = nest.get_sheet_property(sheet, nest.Properties.PIECE_LABEL)
    label = 'abc'
    width = nest.get_sheet_property(sheet, nest.SheetProperties.WIDTH)               #_NSheetWidth
    height = nest.get_sheet_property(sheet, nest.SheetProperties.HEIGHT)             #_NSheetHeight
    #bOk = bOk  AND  NestGetPieceProp( sPiece, _NPieceLabel, &sLabel) ;

    #open table
    line = "<TABLE"
    #start a new page
    if count != 0:
        line += ' style="page-break-before:always"'
    file.write(line)

    #table for customer information - header row
    line = f"""
    <TR>
        <TD rowspan="3">
            <IMG src="{logo}" align="middle">
        </TD>
    </TR>
    <TR>
        <TD>&nbsp;</TD>
    </TR>
    <TR>
        <TD style="font-size:30px" align="right" width="150">Projekt:</TD>
        <TD width="15">&nbsp;</TD>
        <TD style="font-size:30px">{os.path.splitext(project_name)[0]}</TD>
    </TR>
    </TABLE>
    """
    file.write(line)

    #table for sheet information
    line = '<TABLE border="1" cellspacing="1" cellpadding="1">'
    file.write(line)

    #row with sheet name
    line = f'<TR> <TD style="font-size:30px" colspan="6" align="middle">{sheet}</TD>'

    count += 1
    s_count = str(count).zfill(3)

    #adding the barcode
    line += f'<TD id="code{s_count}" colspan="4" class="barcode">{sheet.upper()}</TD>'
    line += '</TR>'
    file.write(line)

    #sheet information - Width, Height, Thickness, Name, Material
    line = f"""
    <TR>
        <TD align="middle">Breite</TD>
        <TD align="middle">{round(width, 2)}</TD>
        <TD align="middle">Höhe</TD>
        <TD align="middle">{round(height, 2)}</TD>
        <TD align="middle">Stärke</TD>
        <TD align="middle">{round(thickness, 2)}</TD>
        <TD align="middle">Name</TD>
        <TD align="middle">{name}</TD>
        <TD align="middle">Material</TD>
        <TD align="middle">{material}</TD>
    </TR>
    """
    file.write(line)

    #picture from the sheet
    #sSizeImg = OPT( nWidth>3*nHeight, "width=^"1200pt^"", "height=^"400pt^"") ;
    size_img = "width=\"1200pt\"" if width > 3 * height else "height=\"400pt\""
    line = f'<TR> <TD colspan="10"> <IMG src="file:///{img_path}"{size_img}> </TD></TR>'
    file.write(line)

    #write down the individual information about the components.
    pieces_on_sheet = nest.get_pieces(sheet)
    n_piece_count = 1
    for piece in pieces_on_sheet:
        line = f"""
        <TR>
            <TD align="middle">Nr.</TD>
            <TD align="middle">{n_piece_count}</TD>
            <TD align="middle">Bezeichnung</TD>
            <TD align="middle">{label}</TD>
            <TD align="middle">Breite</TD>
            <TD align="middle">{width}</TD>
            <TD align="middle">Höhe</TD>
            <TD align="middle">{height}</TD>
        </TR>
        """
        file.write(line)
        n_piece_count += 1

    count_efficiency(file, sheet, sheets, pieces, total_area, curr1, curr2, total_reusable, total_garbage)

    #close table
    line = '</TABLE></BR>'
    file.write(line)

    #update status
    perc = count / n_sheets
    #bOk = bOk  AND  ProgressUpdate( perc) ;   ????????
    count += 1

    insert_java_script(file, count)

    #close HTML
    line = '</BODY></HTML>'
    file.write(line)
    #   bOk = bOk  AND  CloseFile( nFile) ;


def count_efficiency(file, sheet, sheets, pieces, total_area, curr1, curr2, total_reusable, total_garbage):
    do_debug()
    #    autocam_aktivieren = config.get('SETTINGS', 'autocam_aktivieren')
    #    if autocam_aktivieren:
    sheets = nest.get_sheets()

    if sheet:

        file.write(efficiency_for_sheet(pieces, total_area, curr1, curr2))

        #here we do total_efficiency after every sheet was dealt with
        if sheet == sheets[-1]: #if current sheet is the last sheet in list of sheets
            nSheets = len(sheets)
            file.write(efficiency_sheets_total(nSheets, total_area, total_reusable, total_garbage))


def efficiency_for_sheet(pieces, total_area, curr1, curr2):
    return f"""<BR/>
        <BR/>
        <TABLE border="1" cellspacing="1" cellpadding="1">

            <TR>
                <TD style="font-weight: normal;" width="250">Guteile</TD>
                <TD>{pieces}</TD>
            </TR>

            <TR>
                <TD>Gesamtfläche</TD>
                <TD>{round(total_area, 2)}  m²</TD>
            </TR>

            <TR>
                <TD>Nicht wiederverwendbares Material</TD>
                <TD>{round(curr1, 2)}% des Blattes</TD>
            </TR>

            <TR>
                <TD>Wiederverwendbares Material</TD>
                <TD>{round(curr2, 2)}% des Blattes</TD>
            </TR>
        </TABLE>
        """


def efficiency_sheets_total(nSheets, total_area, total_reusable, total_garbage):
    total_garbage /= nSheets #bc I need to not only add % from every sheet but also get the Durchschnitt
    total_reusable /= nSheets
    return f"""<BR/>
        <TABLE border="7" cellspacing="2" cellpadding="3">

            <TR><TH style="font-weight: normal;" align="left">Anzahl Sheets</TH>
                <TH style="font-weight: normal;" colspan="2" align="left"> {nSheets}</TH>
            </TR>

            <TR>
                <TD>Gesamtfläche</TD>
                <TH style="font-weight: normal;" colspan="2" align="left">{round(total_area, 2)} m²</TH>
            </TR>

            <TR>
                <TD>Wiederverwendbares Material pro Blatt im Durchschnitt:</TD>
                <TD>{round(total_reusable, 2)}%</TD>
                <TD>{round(total_area * total_reusable / 100, 2)} m²</TD>
            </TR>

            <TR>
                <TD>Nicht wiederverwendbares Material pro Blatt im Durchschnitt</TD>
                <TD>{round(total_garbage, 2)}%</TD>
                <TD>{round(total_area * total_garbage / 100, 2)} m²</TD>
            </TR>
        </TABLE>
        <BR/>
        """


def html_header_write(project_name):
    return f"""<!DOCTYPE html>
    <html lang="de">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name}</title>
    <script type="text/javascript" src="js/code39.js"></script>
    </head>
    <body>
    """


# def to_pdf():
#     path_to_wkhtmltopdf = r'c:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
#     path_to_html = r'C:\Users\...\Nesting_report\report.html'
#     config = pdfkit.configuratiuon(wkhtmltopdf = path_to_wkhtmltopdf)
#     pdfkit.from_file(path_to_html, output_path = 'report.html', configuration = config)

#    sWkHtmlToPdf = "wkhtmltopdf.exe" ;



if __name__ == '__main__':
    main()
