i_in = int(input("Cati iepuri sunt la inceputul lunii? \t")) #i_in = iepuri la inceput
i_m = int(input("Cati iepuri au murit? \t"))                 #i_n = iepuri morti
i_n = int(input("Cati iepuri s-au nascut? \t"))              #i_m = iepuri nascuti
i_sf = i_in + i_n - i_m                                      #i_sf = iepuri la sfarsitul lunii
print(i_sf, "iepuri sunt la sfarsit de luna")