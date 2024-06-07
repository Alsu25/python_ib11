from docxtpl import DocxTemplate


def create_training_sheet(class_name, subject_name, tpl_name="tpl.docx", *args):
    doc = DocxTemplate(tpl_name)
    args = sorted(args)
    marks = []
    for i in range(len(args)):
        marks.append({'num': i + 1, 'fio': args[i][0], 'mark': args[i][1]})
    context = {'class_name': class_name, 'subject_name': subject_name, 'marks': marks}
    doc.render(context)
    doc.save("res.docx")
