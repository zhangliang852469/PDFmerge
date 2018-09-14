from django.shortcuts import render

from .forms import PdfMergeForm

from django.http import HttpResponse

import PyPDF2

# Create your views here.


def pdf_merge(request):
    if request.method == 'POST':
        # 如果用户通过POST提交
        form = PdfMergeForm(request.POST, request.FILES)

        # 验证表单
        if form.is_valid():
            # 获取表单收集到的内容
            f1 = request.FILES['file1']
            f2 = request.FILES['file2']

            # 转化为PDF 文件对象
            pdfFileObj1 = PyPDF2.PdfFileReader(f1)
            pdfFileObj2 = PyPDF2.PdfFileReader(f2)

            # 创建PDF 文件合并对象
            pdfMerge = PyPDF2.PdfFileMerger()
            pdfMerge.append(pdfFileObj1)
            pdfMerge.append(pdfFileObj2)

            # 将合并文件对象写入pdf合并文件
            with open('merge_file.pdf', 'wb') as pdfOutputFile:
                pdfMerge.write(pdfOutputFile)

            # 打开合并的文件，输出
            with open('merge_file.pdf', 'rb') as merge_file:
                response = HttpResponse(merge_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment: filename= "merge_file.pdf"'
                return response
        else:
            # 如果通过POST提交，表单未通过验证
            form = PdfMergeForm()

        return render(request, 'pdf/pdf_merge.html', {'form': form})