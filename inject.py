import sys

filepath = 'index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = '</section>'
idx = content.find(target)

trust_badges = '''
</section>

<section class="trust-badges fade-in" style="background: #f9f9f9; padding: 40px 5%; text-align: center; border-bottom: 1px solid #ddd;">
    <h3 style="color: #222; font-size: 1.2rem; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px;">Trusted by Vancouver's Best</h3>
    <div style="display: flex; justify-content: center; align-items: center; gap: 40px; flex-wrap: wrap; opacity: 0.8;">
        <div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#d35400" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
            <span style="font-weight: 700; font-size: 0.9rem; color: #222;">WorkSafeBC<br>Compliant</span>
        </div>
        <div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#d35400" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9 12l2 2 4-4"></path></svg>
            <span style="font-weight: 700; font-size: 0.9rem; color: #222;">BBB A+<br>Accredited</span>
        </div>
        <div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#d35400" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            <span style="font-weight: 700; font-size: 0.9rem; color: #222;">Fully Licensed<br>& Insured</span>
        </div>
        <div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#d35400" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
            <span style="font-weight: 700; font-size: 0.9rem; color: #222;">BC Housing<br>Builder</span>
        </div>
    </div>
</section>

<section class="seo-copy fade-in" style="padding: 60px 5%; max-width: 1200px; margin: 0 auto; color: #222;">
    <h2 style="font-size: 2.2rem; margin-bottom: 20px; text-align: center;">Vancouver's Premier General Contracting Firm</h2>
    <p style="margin-bottom: 15px; line-height: 1.8; text-align: center; max-width: 900px; margin-left: auto; margin-right: auto;">Brick Development is the leading <strong>general contractor in Vancouver</strong>, specializing in high-end residential custom homes, commercial build-outs, and major renovations. With over a decade of experience navigating BC's complex zoning bylaws and building codes, our dedicated team of project managers and master craftsmen ensure your project is completed on-time and exactly to specification.</p>
    <div style="display: flex; gap: 15px; flex-wrap: wrap; margin-top: 30px; justify-content: center;">
        <span style="background: #222; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: bold;">Custom Homes</span>
        <span style="background: #222; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: bold;">Commercial Build-Outs</span>
        <span style="background: #222; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: bold;">Laneway Houses</span>
        <span style="background: #222; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: bold;">Structural Renovations</span>
    </div>
</section>
'''

if idx != -1:
    new_content = content[:idx] + trust_badges + content[idx + len(target):]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Injected successfully.")
else:
    print("Could not find hero section closing.")
