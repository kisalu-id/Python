from company import dlg
from sclcore import do_debug
from config import run_config



def main():
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
                pieces = nest.get_sheet_property(sheet, nest.SheetProperties.PIECES_NUMBER)       #_NSheetNumPieces
                curr1 = nest.get_sheet_property(sheet, nest.SheetProperties.RATE_LEFT_OVER)      #_NSheetRateLeftOver  % of sheet   garbage not reusable material
                curr2 = nest.get_sheet_property(sheet, nest.SheetProperties.RATE_REUSABLE)       #_NSheetRateReusable  % of sheet   reusable material
                abfall = area * ( (curr1 + curr2) / 100) #total cut off mat
                total_area += area
                total_left += abfall
                total_garbage += curr1
                total_reusable += curr2
                sC = str(nC).zfill(3)
                nSheets += 1
                nC += 1

                line = f"Sheet{sC} - Material : {matherial}, Länge : {width}, Breite : {height}, Guteile : {pieces}\n"
                file.write(line)

                linetest = f"Efficiency of Sheet{sC} : area {round(area, 2)}, not reusable material curr1 {round(curr1, 2)} (% of sheet),  reusable material curr2 {round(curr2, 2)} (% of sheet), cut off on total: abfall {round(abfall, 2)} mm2???\n\n"
                file.write(linetest)

            file.write(f"Anzahl Sheets : {nSheets}\n")
            file.write(f"Gesamtfläche in m2 : {round(total_area, 2)}\n")
            #file.write(f"Gesamtverschnitt in m2 : {total_left}\n")
            #file.write(f"Prozent Verschnitt : {total_left / total_area * 100}\n")      #dont need that i think, its not saying the impoortant part
            file.write(f"Total garbage not reusable material in m2 : {round(total_garbage / nSheets, 2)}\n"
            file.write(f"Total reusable material in m2 : {round(total_reusable / nSheets, 2)}\n")

            x = 5



if __name__ == '__main__':
    main()
