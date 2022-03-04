# Roadmap

- In case several clients reply "at the same time" the good question should be coordinated by the server.
- Undo the change that the client, when receives an answer, call `processAnswer` conditional if it has answered or not and return to the old that **all** the clients processes (that would facilitate the coordinations by the Server as the previou point). To do that, `I_HAVE_ANSWERED` should have three values : null /true / false and ththen when `processAnswer` is called twice by the client answering:
 - First time `I_HAVE_ANSWERED` is null and the function is called with parameter iHaveAnswered = true => update `I_HAVE_ANSWERED` and send message to the server
 - Second time `I_HAVE_ANSWERED` is true and the function is called with parameter iHaveAnswered = false => not update `I_HAVE_ANSWERED` and call markAnswer
- For the other clients it is called only once
 - First (unique) time `I_HAVE_ANSWERED` is null and the function is called with parameter iHaveAnswered = false => update `I_HAVE_ANSWERED` and call markAnswer
- Maybe it is more verbose but more clear if:
  - Put back the set `I_HAVE_ANSWERED` in its right place (as it is)
  - Change the parameter `iHaveAnswered` by `isRemoteAnswer` => still not nice with the poor client that has answered ...
