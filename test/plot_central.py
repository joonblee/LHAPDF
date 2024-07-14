import matplotlib.pyplot as plt
import numpy as np
import lhapdf

# Load PDF set
print("Print PDF sets")
pdfset_ct18 = lhapdf.getPDFSet("CT18NNLO")
pdf_ct18 = pdfset_ct18.mkPDF(0)

pdfset_nnpdf = lhapdf.getPDFSet("NNPDF40_nnlo_as_01180")
pdf_nnpdf = pdfset_nnpdf.mkPDF(0)

pdfset_msht20 = lhapdf.getPDFSet("MSHT20nnlo_as118")
pdf_msht20 = pdfset_msht20.mkPDF(0)


# Define the Q^2 value
Q2 = 10 

# x values
#x_values = np.logspace(-2, 0, 100) # Generates 100 points between 10^-2 and 10^0, logarithmically spaced
x_values = [x * 0.01 for x in range(1, 100)]

# Calculate d and u quark PDF values for CT18NNLO
d_values_ct18 = [pdf_ct18.xfxQ2(1, x, Q2) for x in x_values] # d-quark
u_values_ct18 = [pdf_ct18.xfxQ2(2, x, Q2) for x in x_values] # u-quark
dbar_values_ct18 = [pdf_ct18.xfxQ2(-1, x, Q2) for x in x_values] # d-quark
ubar_values_ct18 = [pdf_ct18.xfxQ2(-2, x, Q2) for x in x_values] # u-quark

# Calculate d and u quark PDF values for NNPDF4.0 NLO
d_values_nnpdf = [pdf_nnpdf.xfxQ2(1, x, Q2) for x in x_values] # d-quark
u_values_nnpdf = [pdf_nnpdf.xfxQ2(2, x, Q2) for x in x_values] # u-quark
dbar_values_nnpdf = [pdf_nnpdf.xfxQ2(-1, x, Q2) for x in x_values] # d-quark
ubar_values_nnpdf = [pdf_nnpdf.xfxQ2(-2, x, Q2) for x in x_values] # u-quark

# Calculate d and u quark PDF values for MSHT20
d_values_msht20 = [pdf_msht20.xfxQ2(1, x, Q2) for x in x_values] # d-quark
u_values_msht20 = [pdf_msht20.xfxQ2(2, x, Q2) for x in x_values] # u-quark
dbar_values_msht20 = [pdf_msht20.xfxQ2(-1, x, Q2) for x in x_values] # d-quark
ubar_values_msht20 = [pdf_msht20.xfxQ2(-2, x, Q2) for x in x_values] # u-quark



# Calculate d/u ratio
du_ratio_ct18 = [d/u for d, u in zip(d_values_ct18, u_values_ct18)]
du_ratio_nnpdf = [d/u for d, u in zip(d_values_nnpdf, u_values_nnpdf)]

ubaru_ratio_ct18 = [ubar/u for ubar, u in zip(ubar_values_ct18, u_values_ct18)]
ubaru_ratio_msht20 = [ubar/u for ubar, u in zip(ubar_values_msht20, u_values_msht20)]
ubaru_ratio_nnpdf = [ubar/u for ubar, u in zip(ubar_values_nnpdf, u_values_nnpdf)]
dbard_ratio_ct18 = [dbar/d for dbar, d in zip(dbar_values_ct18, d_values_ct18)]
dbard_ratio_msht20 = [dbar/d for dbar, d in zip(dbar_values_msht20, d_values_msht20)]
dbard_ratio_nnpdf = [dbar/d for dbar, d in zip(dbar_values_nnpdf, d_values_nnpdf)]

# Plot
print("Draw plots")
plt.figure(figsize=(8, 6))
plt.plot(x_values, du_ratio_nnpdf, label='NNPDF40_nlo_as_0118', color='red')
plt.plot(x_values, du_ratio_ct18, label='CT18NLO', color='blue')
plt.title(f'd/u Ratio at $Q^2 = {Q2} \, \mathrm{{GeV}}^2$')
plt.xlabel('$x$')
plt.ylabel('$d/u$ ratio')
#plt.xscale('log')
plt.yscale('log')
plt.xlim(0.,1.)
#plt.ylim(0.,1.)
plt.ylim(0.03,1.)
plt.legend()
plt.grid(True, which="both", ls="--") # Add grid for better readability
plt.savefig(f'du_ratio{Q2}.png')
#plt.show()

plt.figure(figsize=(8, 6))
plt.plot(x_values, dbard_ratio_nnpdf, label='NNPDF40_nnlo_as_0118 ($\\bar{{d}}/d$)', color='red')
plt.plot(x_values, ubaru_ratio_nnpdf, label='NNPDF40_nnlo_as_0118 ($\\bar{{u}}/u$)', color='red', linestyle='--')
plt.plot(x_values, dbard_ratio_msht20, label='MSHT20nnlo_as118 ($\\bar{{d}}/d$)', color='blue')
plt.plot(x_values, ubaru_ratio_msht20, label='MSHT20nnlo_as118 ($\\bar{{u}}/u$)', color='blue', linestyle='--')
plt.plot(x_values, dbard_ratio_ct18, label='CT18NNLO ($\\bar{{d}}/d$)', color='green')
plt.plot(x_values, ubaru_ratio_ct18, label='CT18NNLO ($\\bar{{u}}/u$)', color='green', linestyle='--')
plt.title(f'$\\bar{{q}}/q$ Ratio at $Q^2 = {Q2} \, \mathrm{{GeV}}^2$')
plt.xlabel('$x$')
plt.ylabel('$\\bar{{q}}/q$ ratio')
#plt.xscale('log')
plt.yscale('log')
plt.xlim(0.,1.)
#plt.ylim(0.,1.)
plt.ylim(0.00001,2.)
plt.legend()
plt.grid(True, which="both", ls="--") # Add grid for better readability
plt.savefig(f'qbarq_ratio{Q2}.png')

plt.figure(figsize=(8, 6)) 
plt.plot(x_values, u_values_ct18, label='CT18NLO (u)', color='red')
plt.plot(x_values, d_values_ct18, label='CT18NLO (d)', color='red',linestyle='--')
plt.plot(x_values, u_values_nnpdf, label='NNPDF40 (u)', color='blue')
plt.plot(x_values, d_values_nnpdf, label='NNPDF40 (d)', color='blue',linestyle='--')
plt.title(f'PDFs at $Q^2 = {Q2} \, \mathrm{{GeV}}^2$')
plt.xlabel('$x$')
plt.ylabel('PDF')
#plt.xscale('log')
plt.xlim(0.,1.)
plt.ylim(0.,0.7)
plt.legend()
plt.grid(True, which="both", ls="--") # Add grid for better readability
plt.savefig(f'pdf{Q2}.png')

print("++ done ++")
