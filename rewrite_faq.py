import os

faqs = [
    ("What areas do you service?", "We proudly service the entire Greater Vancouver Area, including Vancouver, North Vancouver, West Vancouver, Burnaby, Richmond, Coquitlam, Surrey, Langley, and New Westminster."),
    ("Do you handle building permits?", "Yes, we handle the entire permitting process with the City of Vancouver and surrounding municipalities, ensuring your project is fully compliant before construction begins."),
    ("Are you WorkSafeBC licensed?", "Absolutely. We are fully licensed, insured, and WorkSafeBC compliant. Safety on the job site is our number one priority."),
    ("Do you offer a new home warranty?", "Yes, as a licensed residential builder in British Columbia, all of our new custom homes are covered under the mandatory 2-5-10 Year Home Warranty Insurance."),
    ("How much does a custom home cost per square foot?", "Costs vary heavily depending on materials, site conditions, and finishes, but typically range from  to + per square foot in the Vancouver market."),
    ("How long does a custom home build take?", "On average, a custom home in Vancouver takes between 10 to 16 months to complete, depending on the size, complexity, and the municipal permitting timeline."),
    ("Can you help with architectural design?", "Yes, we partner with some of the top architectural and interior design firms in Vancouver. We can either work with your existing plans or connect you with our design partners."),
    ("Do you do commercial renovations?", "Yes, we specialize in high-end commercial renovations, including restaurants, bars, cafes, retail boutiques, and modern office build-outs."),
    ("What is a tenant improvement (TI)?", "A tenant improvement is a custom interior build-out of a commercial space to meet the specific needs of a business. We manage TI projects from framing to final finishing."),
    ("Can I live in my home during a renovation?", "This depends on the scale of the renovation. For major gut-renovations or structural additions, we highly recommend relocating for safety and speed. For smaller projects, we try to accommodate living on-site when safe."),
    ("Do you work with subcontractors?", "Yes, we manage a highly vetted roster of specialized sub-trades (plumbers, electricians, HVAC). Our in-house project managers oversee their work daily to ensure uncompromising quality."),
    ("How do you handle change orders?", "If you decide to change the scope of work during construction, we will provide a detailed Change Order outlining the cost and timeline impact for your approval before proceeding."),
    ("What is your payment schedule?", "We use a transparent progress billing system. Payments are tied to specific construction milestones (e.g., foundation poured, framing completed) so you only pay for work that has been completed."),
    ("Do you do laneway homes?", "Yes, we design and build custom laneway homes, which are an excellent way to maximize property value and generate rental income in Vancouver."),
    ("Are your estimates free?", "Yes, we provide complimentary initial consultations and high-level estimates for serious inquiries."),
    ("Do you specialize in heritage restorations?", "Yes, we have extensive experience navigating Vancouver's heritage building bylaws and restoring historical properties while modernizing their structural integrity."),
    ("Can you do seismic upgrades?", "Absolutely. Seismic upgrading is a crucial part of major renovations in the Pacific Northwest, and we ensure your home meets the latest earthquake safety codes."),
    ("What kind of materials do you use?", "We use premium, durable materials suited for the Pacific Northwest climate, ranging from imported stone and custom glass to sustainable local timber."),
    ("Do you offer landscaping services?", "Yes, we offer comprehensive luxury landscaping, including architectural concrete retaining walls, driveway paving, and custom outdoor living spaces."),
    ("Will there be a dedicated project manager?", "Yes, your project will be assigned a dedicated Project Manager who will be your main point of contact and will provide you with weekly progress updates.")
]

faq_html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Frequently Asked Questions | Brick Development</title>
    <link rel="stylesheet" href="/bricks-dev-live/assets/css/style.css">
    <style>
        .faq-item {
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }
        .faq-item h3 {
            color: var(--primary);
            margin-bottom: 10px;
            font-size: 1.3rem;
        }
        .faq-item p {
            color: var(--text-light);
            line-height: 1.8;
            font-size: 1.05rem;
        }
    </style>
</head>
<body>
    <header>
        <div class="logo"><a href="/bricks-dev-live/index.html"><img src="/bricks-dev-live/assets/images/brick-development-general-contractor-vancouver-logo.jpg" alt="Brick Development Logo"></a></div>
        <ul class="nav-links">
            <li><a href="/bricks-dev-live/index.html">Home</a></li>
            <li><a href="/bricks-dev-live/about.html">About</a></li>
            <li><a href="/bricks-dev-live/services.html">Services</a></li>
            <li><a href="/bricks-dev-live/projects.html">Projects</a></li>
            <li><a href="/bricks-dev-live/contact.html">Contact</a></li>
        </ul>
    </header>
    
    <section class="container fade-in" style="margin-top: 100px; min-height: 60vh; max-width: 900px;">
        <h1 style="color: var(--primary); text-align: center; margin-bottom: 10px;">Frequently Asked Questions</h1>
        <p style="text-align: center; color: var(--text-light); margin-bottom: 50px;">Everything you need to know about building and renovating with Brick Development.</p>
        
        <div class="faq-list">
'''

for q, a in faqs:
    faq_html_content += f'''
            <div class="faq-item">
                <h3>{q}</h3>
                <p>{a}</p>
            </div>
'''

faq_html_content += '''
        </div>
    </section>
'''

# Get standard footer
footer_html = ""
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()
    if '<footer' in idx:
        footer_html = '<footer' + idx.split('<footer')[1]

faq_html_content += footer_html

with open('faq.html', 'w', encoding='utf-8') as f:
    f.write(faq_html_content)

print("Rewrote faq.html to display realistic Q&A content instead of links.")