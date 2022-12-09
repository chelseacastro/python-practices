data_berita = 'Instagram merintis fitur NFT sejak Maret tahun ini. Per Mei lalu, fitur ini baru tersedia terbatas di beberapa negara bagian di AS. Kemudian pada 4 Agustus 2022, masyarakat Indonesia bersama dengan 100 negara lain di Amerika, Asia Pasifik, Afrika, dan Timur Tengah, sudah dapat memamerkan koleksi NFT mereka melalui akun Instagram masing-masing. Pengguna dapat memamerkan NFT koleksi mereka di Feed, Story hingga Direct Message. Pengguna bahkan dapat menampilkan NFT sebagai augmented reality di Story. Kreator NFT dan pemilik akan otomatis di tag dan ada informasi terkait koleksi NFT yang ditampilkan.Pengguna hanya harus menghubungkan dompet kripto mereka dengan akun Instagram. Dompet yang mendukung antara lain Rainbow, MetaMask, Trust Wallet, Coinbase Wallet dan Dapper Wallet. Sementara blockchain-nya adalah Ethereum, Polygon dan Flow. Fitur ini belum termasuk pada jual beli NFT, namun Meta mengatakan sedang menuju tujuan tersebut. NFT telah membuka pintu peluang baru bagi saya dan artis lain di seluruh dunia. Teknologi baru ini memberi kami outlet lain untuk mencari nafkah dan terhubung dengan penggemar dan kolektor kami, ujar fotografer sekaligus pemilik NFT asal AS Natalie Amrossi, dikutip dari halaman resmi Instagram. Sebagai perayaan masuknya fitur NFT di Instagram Indonesia, seorang kreator NFT Sultan Gustaf Al Ghozali, merilis NFT khusus berupa foto dirinya memegang logo Instagram. NFT ini kemudian dibeli dan diunggah di feed Pieter Lydian, Country Director Facebook untuk Indonesia. Kami berharap fitur ini bisa membuka peluang yang lebih besar lagi untuk para kreator memonetisasi kreativitas mereka di Instagram, serta mendukung peluang ekonomi yang akan diberikan oleh Metaverse untuk Indonesia, ungkapnya dalam caption tersebut. Meta meyakini dukungan NFT dan blockchain di ekosistem Meta akan mendukung kreator dan pelaku bisnis, mulai dari menghasilkan inovasi dan melahirkan konten kreatif dengan biaya minimum.'

def hitung_kata(panjang,kata):
    data = {
        "panjang huruf":panjang,
        "kata":kata
    }
    return data

list = []
for x in data_berita.split(" "):
    list.append(len(x))

list_set = set(list)
unique = []
for x in list_set:
    unique.append(x)
print(unique)

for x in unique:
    list_kata = []
    for y in data_berita.split(" "):
        if x == len(y):
            list_kata.append(y)
    print(hitung_kata(x,set(list_kata)))
