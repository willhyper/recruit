# recruit

a little humor about how using thread resembles doing a work by self, by contractor, or by full time employee.

```python

python -m test.test_recruit
```
generates

```
<recruit.self.Self> takes job in 0.30 s, and finishes job with result 832040 in 1.0e-05 s
```
when you assign youself a work, you start doing it when assigned. Asking result barely takes extra time.

```
<recruit.contractor.Contractor> takes job in 0.0066 s, and finishes job with result 832040 in 0.299 s
```
when assigning a job to a contractor, you hire him first. You move on and ask result later. once done, the contract terminates.

```
<recruit.fulltime_employee.FullTimeEmployee> takes job in 3.02e-05 s, and finishes job with result 832040 in 0.304 s
```
when assigning a job to a full time employee, you put the job onto his queue and move on. The employee takes job from queue, otherwise stay idle.
