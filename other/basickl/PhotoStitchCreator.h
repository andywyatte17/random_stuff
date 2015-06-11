//
// PhotoStitchCreator.h
//
// AStyle - Linux, indent = 2 spaces
//

#pragma once

#include <stdint.h>
#include <cmath>

#define VSM_ASSERT(a,b) do {} while(0)

#include <list>

struct PointI {
  int32_t x,y;
  bool operator==(const PointI& rhs) const
  {
    return x==rhs.x && y==rhs.y;
  }
};

inline double hypot(double dx, double dy)
{
  return sqrt(dx*dx+dy*dy);
}

struct Node {
  PointI pt;
  Node* prev = nullptr;
  Node* next = nullptr;
  double distToNextPt = 0;
  void SetPrev(Node* prev0)
  {
    prev = prev0;
  }
  void SetNext(Node* next0)
  {
    next = next0;
    if( ! next )
      distToNextPt = -1;
    else
      distToNextPt = hypot(pt.x-next->pt.x, pt.y-next->pt.y);
  }
};

double TryReverseSection(Node *nodes);

// Remarks:
// The idea is based on the article "An Effective Implementation of the Lin-Kernighan Traveling Salesman Heuristic"
// by Keld Helsgaun, European Journal of Operational Research 126 (1): 106-130. Only the simplest optimization,
// 2-opt move, has been used.
//
template<class PointI_Container_t>
void BasicLK(PointI_Container_t &chain, int threshold)
{
  struct DbxVars {
    unsigned c = 0;
    void operator++()
    {
      ++c;
    }
  };

  DbxVars improveLoop, distanceTests;

  if(chain.empty())
    return;

  int nCount=(int)chain.size();
  Node* nodes=new Node[nCount];
  {
    // convert the content of CList to the Node array
    Node *pNode0=nullptr,*pNode1=&(nodes[0]);
    auto it=chain.begin();
    pNode1->pt=*(it++);
    pNode1->prev=pNode0;
    pNode0=pNode1;
    pNode1++;
    while(it!=chain.end()) {
      pNode1->pt=*(it++);
      pNode1->SetPrev(pNode0);
      pNode0->SetNext(pNode1);
      pNode0=pNode1;
      pNode1++;
    }
    pNode0->next=nullptr;
    pNode0->distToNextPt=-1;
  }

  double totalGain=0; // report totally how much gain has been obtained through this optimization
  totalGain+=TryReverseSection(nodes);  // consider a section direction swap

  // start with an initial tour that is roughly good but needs further improvement
  double gain;
  bool bImproved=true;
  double d0,d1,d2,d3;
  double d0sq,d1sq;
  Node *pNode,*pNode0,*pNode1,*pNode2,*pNode3=nullptr;
  Node *pNodeT;
  bool bPassSection12=false;
  while(bImproved) {
    ++improveLoop;
    bImproved=false;
    pNode0=&(nodes[0]);         // the starting node is never moved
    while(pNode0->next!=nullptr) {
      pNode1=pNode0->next;
      d0=pNode0->distToNextPt;
      if(d0>threshold) { // here we use 4.0mm as the threshold for starting process
        // for each long jump (>4.0mm), do following processing
        // Now we have the X1(t1-t2), so need to choose Y1(t2-t3). t3 could be anywhere in the chain, as long as
        //  t3 is not next to t2 in the chain, and dist(t2-t3)<dist(t1-t2).
        d0sq=d0*d0;
        pNode2=&(nodes[0]);
        bPassSection12=false;
        gain=0;
        while(pNode2->next!=nullptr) {
          pNode3=pNode2->next;
          if((pNode2==pNode1) || (pNode2==pNode0)) {
            bPassSection12=true;
            pNode2=pNode3;
            continue;
          }
          ++distanceTests;
          d1sq=(pNode3->pt.x-pNode1->pt.x)*(pNode3->pt.x-pNode1->pt.x)+
               (pNode3->pt.y-pNode1->pt.y)*(pNode3->pt.y-pNode1->pt.y);
          if(d1sq<d0sq) {
            d1=sqrt(d1sq);
            d2=pNode2->distToNextPt;
            d3=sqrt(double((pNode2->pt.x-pNode0->pt.x)*(pNode2->pt.x-pNode0->pt.x)+
                           (pNode2->pt.y-pNode0->pt.y)*(pNode2->pt.y-pNode0->pt.y)));
            gain=d0-d1+d2-d3;
            if(gain>1) break; // only worth considering when gain is bigger than 0.1mm
          }
          pNode2=pNode3;
        }
        if(gain>1) {
          // rebuild the chain
          if(bPassSection12) { // in the order of pNode0, pNode1, pNode2, pNode3
            // pointing pNode0 to pNode2, reverse the nodes starting from pNode2 backwards till pNode1,
            // pointing pNode1 to pNode3
            pNode0->SetNext(pNode2);
            pNode=pNode2;
            pNode->SetNext(pNode0); // wait for reversing in the do{}while loop
            do {
              pNodeT=pNode->next;
              pNode->SetNext(pNode->prev);
              pNode->SetPrev(pNodeT);
              pNode=pNode->next;
            } while(pNode!=pNode1);
            VSM_ASSERT(pNode==pNode1, "");
            pNode->SetPrev(pNode->next);
            pNode->SetNext(pNode3);
            pNode3->SetPrev(pNode1);
          } else {              // in the order of pNode2, pNode3, pNode0, pNode1
            // pointing pNode2 to pNode0, reverse the nodes starting from pNode0 backwards till pNode3,
            // pointing pNode3 to pNode1
            pNode2->SetNext(pNode0);
            pNode=pNode0;
            pNode->SetNext(pNode2);
            do {
              pNodeT=pNode->next;
              pNode->SetNext(pNode->prev);
              pNode->SetPrev(pNodeT);
              pNode=pNode->next;
            } while(pNode!=pNode3);
            VSM_ASSERT(pNode==pNode3, "");
            pNode->SetPrev(pNode->next);
            pNode->SetNext(pNode1);
            pNode1->SetPrev(pNode3);
          }
          bImproved=true;
          totalGain+=gain;
          break;
        }
      }
      pNode0=pNode1;
    }
  }

  double newGain=TryReverseSection(nodes);  // consider a section direction swap
  totalGain+=newGain;
  newGain=TryReverseSection(nodes);         // consider a section direction swap
  totalGain+=newGain;
  newGain=TryReverseSection(nodes);         // consider a section direction swap
  totalGain+=newGain;

  {
    // transfer the result back
    Node *pNode=&(nodes[0]);
    auto it=chain.begin();
    while(pNode!=nullptr) {
      *it=pNode->pt;
      it++;
      pNode=pNode->next;
    }
  }

  delete [] nodes; // clean up
}

// Description:
// Try reversing each section in the path. If it creates a shorter total path length, use it
//
inline double TryReverseSection(Node *nodes)
{
  double newGain=0.0;
  double dOld,dNew;
  Node *pNode0=&(nodes[0]);
  Node *pNode1,*pNode2,*pNode3;
  int32_t dist02sq,dist13sq;
  while(pNode0!=nullptr) {
    pNode1=pNode0->next;
    if(pNode1==nullptr) break;
    pNode2=pNode1->next;
    if(pNode2==nullptr) break;
    pNode3=pNode2->next;
    if(pNode3==nullptr) break;
    dOld=pNode0->distToNextPt+pNode2->distToNextPt;
    dist02sq=(pNode0->pt.x-pNode2->pt.x)*(pNode0->pt.x-pNode2->pt.x)+(pNode0->pt.y-pNode2->pt.y)*(pNode0->pt.y-pNode2->pt.y);
    dist13sq=(pNode1->pt.x-pNode3->pt.x)*(pNode1->pt.x-pNode3->pt.x)+(pNode1->pt.y-pNode3->pt.y)*(pNode1->pt.y-pNode3->pt.y);
    dNew=sqrt(double(dist02sq))+sqrt(double(dist13sq));
    if(dNew<dOld) {
      newGain+=dOld-dNew;
      pNode0->SetNext(pNode2);
      pNode2->SetPrev(pNode0);
      pNode2->SetNext(pNode1);
      pNode1->SetPrev(pNode2);
      pNode1->SetNext(pNode3);
      pNode3->SetPrev(pNode1);
    }
    pNode0=pNode0->next;
  }
  return newGain;
}
