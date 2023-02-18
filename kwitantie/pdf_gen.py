from fpdf import FPDF
from datetime import datetime
from .input_fields import user_contact_details


def make_pdf(kwitantie):
    pdf = FPDF()
    pdf.set_author(user_contact_details()["user_name"])
    pdf.add_page()

    pdf.set_fill_color(238, 238, 238)
    pdf.rect(30, 115, 110, 8, style='F')
    pdf.rect(30, 124, 106, 88, style='F')
    pdf.rect(137, 115, 22, 97, style='F')
    pdf.rect(160, 115, 19, 97, style='F')
    pdf.rect(180, 115, 19, 97, style='F')
    pdf.rect(170, 213, 29, 8, style='F')

    pdf.set_font('Helvetica', 'B', 24)
    pdf.text(110, 20, 'Kwitantie')

    pdf.set_font('Helvetica', '', 10)
    pdf.text(110, 40, 'Kwitantienummer')
    pdf.text(155, 40, kwitantie.kwitantienummer)
    pdf.text(110, 45, 'Datum')
    pdf.text(155, 45, datetime.now().strftime("%d-%m-%Y"))

    pdf.text(30, 40, user_contact_details()["user_name"])
    pdf.text(30, 45, user_contact_details()["user_straat"])
    pdf.text(30, 50, "%s %s" % (user_contact_details()["user_postcode"],
                                user_contact_details()["user_plaats"]))
    pdf.text(30, 55, "Nederland")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.text(30, 65, "Aan:")

    pdf.set_font('Helvetica', '', 10)
    pdf.text(30, 70, kwitantie.naam)
    pdf.text(30, 75, "%s %s" % (kwitantie.straat, kwitantie.nummer))
    pdf.text(30, 80, "%s %s" % (kwitantie.postcode, kwitantie.plaats))
    pdf.text(30, 85, "Nederland")

    pdf.line(10, 100, 200, 100)
    pdf.line(10, 265, 200, 265)

    pdf.text(30, 110, "Geleverde dienst:")
    pdf.text(143, 110, "Tarief")
    pdf.text(163, 110, "Uren")
    pdf.text(183, 110, "Totaal")

    pdf.text(35, 120, kwitantie.dienst)
    pdf.set_font('Helvetica', '', 8)
    pdf.text(142, 120, "EUR %.2f" % kwitantie.bedrag)
    pdf.text(166, 120, str(kwitantie.aantal_uren))
    pdf.text(182, 120, "EUR %.2f" % (kwitantie.bedrag * float(kwitantie.aantal_uren)))

    pdf.set_font('Helvetica', 'B', 8)
    pdf.text(35, 130, "Beschrijving : ")

    pdf.set_font('Helvetica', '', 8)
    pdf.text(35, 135, kwitantie.beschrijving[:70])
    pdf.text(35, 140, kwitantie.beschrijving[71:140])
    pdf.text(35, 145, kwitantie.beschrijving[141:210])
    pdf.text(35, 150, kwitantie.beschrijving[211:280])
    pdf.text(35, 155, kwitantie.beschrijving[281:350])
    pdf.text(35, 160, kwitantie.beschrijving[351:420])
    pdf.text(35, 165, kwitantie.beschrijving[421:490])
    pdf.text(35, 170, kwitantie.beschrijving[491:560])
    pdf.text(35, 175, kwitantie.beschrijving[561:630])
    pdf.text(35, 180, kwitantie.beschrijving[631:700])

    pdf.set_font('Helvetica', '', 11)
    pdf.text(155, 218, "Totaal ")
    pdf.text(175, 218, "EUR %.2f" % (kwitantie.bedrag * float(kwitantie.aantal_uren)))

    pdf.text(30, 273, "Handtekening : ")
    try:
        pdf.image(user_contact_details()["user_signature_location"], 30, 274, 30)
    except:
        pass
    pdf.text(100, 273, "Gelieve te voldoen op het volgende rekeningnummer:")
    pdf.text(125, 278, "NL 00 BNK 000 123 45 67 t.a.v J Doe")

    pdf.output('kwitantie-%s.pdf' % kwitantie.kwitantienummer)
    return kwitantie.kwitantienummer
