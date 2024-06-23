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

if __name__ == '__main__':
    main()
