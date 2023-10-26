def konversi(j=0):
    def minggu(w=0):
        def hari(h=0):
            def jam(m=0):
                def menit(d=0):
                    return (((j * 7 + w) * 24 + h) * 60 + m) * 60 + d
                return menit
            return jam
        return hari
    return minggu

data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

filter_data = []

for item in data:
    parts = item.split()
    nilai_filter = list(filter(str.isdigit, parts))
    filter_data.append(nilai_filter)

for values in filter_data:
    print(values)
