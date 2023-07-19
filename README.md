# Prime Test Validation for Arxiv 2307.09009

I built this quickly to do some validation of the results of https://arxiv.org/pdf/2307.09009.pdf

The authors do not reveal their system prompt. However, they do reveal a temperature (0.1). 

Their results for their full dataset was: ![](prime-results-2307-09009.png)

In my test, I had these results: ![](results.png)

Notably, I did two things definitely different from their results:

# I used a system message of `p.messages = [{"role":"system", "content": "You are an expert mathematician and careful reasoner that produces highly accurate results."}]`
# I used temperature=0

I used gpt sandbox to normalize the answer (ie pulling [Yes] [No] from the long string), and to generate the graph.


