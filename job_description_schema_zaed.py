from pydantic import BaseModel, Field
# use this virtual envn -> reflection_env

class Responsibility(BaseModel):
    """Represents a key responsibility of the position"""
    name: str = Field(description="Sell Beauty Products")
    type: str = Field(description="Beauty")
    description: str = Field(default=None, description="The ideal Salesperson is passionate about fashion and styling and has the ability to cultivate and grow a customer following, both digitally and in-store.")

class Skill(BaseModel):
    """Represents a required skill for the position"""
    name: str = Field(description="Excellent communication and people skills")
    type: str = Field(description="Soft Skill")
    role: str = Field(description="Beauty Salesperson")
    difficulty_level: str = Field(description="Intermediate")

class SalaryInfo(BaseModel):
    """Represents compensation details"""
    hourly_rate: float = Field(default=None, description= "Hourly wage")
    hourly_range_min: int = Field(default=None, description= 16)
    hourly_range_max: int = Field(default=None, description= 20)
    annual_salary: str = Field(default=None, description="$20,000 - $40,000 a year")
    commission: float= Field(default=None, description="Commissions")
    currency: str = Field(default="USD", description="Currency of compensation")

class JobDescription(BaseModel):
    """Complete job description schema"""
    job_title: str = Field(description="Retail Sales - Accessories")
    company: str = Field(description="Sephora")
    location: str = Field(description="Schaumburg, IL")
    posting_date: str = Field(default=None, description="Indeed")
    employment_type: str = Field(default=None, description="Part-Time")
    
'''
Job Description Example:
Retail Sales - Accessories - Woodfield Shopping Center- job post
Nordstrom
3.8
3.8 out of 5 stars
Schaumburg, IL 60173
$16.85 an hour
Nordstrom
Schaumburg, IL 60173
$16.85 an hour
Job details
Here’s how the job details align with your profile.
Pay

$16.85 an hour
Encouraged to apply
Fair chance
&nbsp;
Benefits
Pulled from the full job description
401(k)
Health insurance
Paid time off
Vision insurance
Dental insurance
Life insurance
Employee assistance program
Disability insurance
Store discount
&nbsp;
Full job description
The ideal Salesperson is passionate about fashion and styling and has the ability to cultivate and grow a customer following, both digitally and in-store.

A day in the life…

Set and achieve sales goals, for both in-store and digital selling with effective use of selling tools (inclusive of text and social media)
Build lasting relationships with customers
Give the best service to our customers on their terms
Provide honest and confident feedback to customers about style and fit
Seek fashion and product knowledge to build your expertise
Work with the team to keep the department customer ready, which means filling orders, stocking, re-merchandising, price markdowns, and light cleaning
Grow relationships by opening new Nordstrom Rewards program accounts
The hours and schedule for this position will vary by week depending on business needs
This role may require you to be flexible to occasionally performing work/duties in a department other than the one you were hired into
You own this if you have…

Excellent communication and people skills
A self-motivated, goal oriented focus
Strong interest to use networking and technology to achieve sales goals
The ability to excel in a team environment
The ability to prioritize multiple tasks in a fast-paced environment
Organization and follow through
The ability to work a flexible schedule based on business needs
Physical Requirements:
Continuous movement for 6-8 hours per shift, which includes frequent bending, twisting, squatting, flexing and reaching in order to handle merchandise and assist customers.
Frequent use of hands for grasping, fine manipulation, pushing and pulling
Handle bulky and sometimes awkwardly shaped items, which includes reaching for and lifting these items above the head.
Regularly lift items weighing up to 10 pounds and occasionally up to 25 pounds
We’ve got you covered…

Our employees are our most important asset and that’s reflected in our benefits. Nordstrom is proud to offer a variety of benefits to support employees and their families, including:

Medical/Vision, Dental, Retirement and Paid Time Away

Life Insurance and Disability

Merchandise Discount and EAP Resources

A few more important points...

The job posting highlights the most critical responsibilities and requirements of the job. It’s not all-inclusive. There may be additional duties, responsibilities and qualifications for this job.

For Los Angeles or San Francisco applicants: Nordstrom is required to inform you that we conduct background checks after conditional offer and consider qualified applicants with criminal histories in a manner consistent with legal requirements per Los Angeles, Cal. Muni. Code 189.04 and the San Francisco Fair Chance Ordinance. For additional state and location specific notices, please refer to the Legal Notices document within the FAQ section of the Nordstrom Careers site.

Applicants with disabilities who require assistance or accommodation should contact the nearest Nordstrom location, which can be identified at www.nordstrom.com.

Please be mindful that there may be legal notices and requirements related to this job posting that are specific to your state. Review the Career Site FAQ’s for relevant information and guidelines.

© 2022 Nordstrom, Inc

Current Nordstrom employees: To apply, log into Workday, click the Careers button and then click Find Jobs.

Applications are accepted on an ongoing basis.

Pay Range Details

The pay range(s) below has been provided in compliance with state specific laws. Pay ranges may be different for other locations.
Pay offers are dependent on the location, as well as job-related knowledge, skills, and experience.

$16.85 - $16.85 Hourly
This position may be eligible for performance-based incentives/bonuses. Benefits include 401k, medical/vision/dental/life/disability insurance options, PTO accruals, Holidays, and more. Eligibility requirements may apply based on location, job level, classification, and length of employment. Learn more in the Nordstrom Benefits Overview by copying and pasting the following URL into your browser: https://careers.nordstrom.com/pdfs/Ben_Overview_07-14_Variable_ES-US.pdf
At Nordstrom, the commission most selling employees receive varies based on the merchandise they sell. Apparel, shoes, and accessories sales typically range from 3% to 14.5%. The commission Beauty and Men’s Fragrance sales roles typically receive is 3%.
'''