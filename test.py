from tokenizer import Tokenizer

if __name__=="__main__":
    tokenizer = Tokenizer(c_str="""RewriteUsesOfClonedInstructions(BasicBlock *OrigHeader,
                                            BasicBlock *OrigPreheader,
                                            ValueToValueMapTy &ValueMap) {
    // Remove PHI node entries that are no longer live.
    BasicBlock::iterator I, E = OrigHeader->end();
    for (I = OrigHeader->begin(); PHINode *PN = dyn_cast<PHINode>(I); ++I)
        PN->removeIncomingValue(PN->getBasicBlockIndex(OrigPreheader));

    // Now fix up users of the instructions in OrigHeader, inserting PHI nodes
    // as necessary.
    SSAUpdater SSA;
    for (I = OrigHeader->begin(); I != E; ++I) {
        Value *OrigHeaderVal = &*I;

        // If there are no uses of the value (e.g. because it returns void), there
        // is nothing to rewrite.
        if (OrigHeaderVal->use_empty())
        continue;

        Value *OrigPreHeaderVal = ValueMap[OrigHeaderVal];

        // The value now exits in two versions: the initial value in the preheader
        // and the loop "next" value in the original header.
        SSA.Initialize(OrigHeaderVal->getType(), OrigHeaderVal->getName());
        SSA.AddAvailableValue(OrigHeader, OrigHeaderVal);
        SSA.AddAvailableValue(OrigPreheader, OrigPreHeaderVal);

        // Visit each use of the OrigHeader instruction.
        for (Value::use_iterator UI = OrigHeaderVal->use_begin(),
            UE = OrigHeaderVal->use_end(); UI != UE; ) {
        // Grab the use before incrementing the iterator.
        Use &U = *UI;

        // Increment the iterator before removing the use from the list.
        ++UI;

        // SSAUpdater can't handle a non-PHI use in the same block as an
        // earlier def. We can easily handle those cases manually.
        Instruction *UserInst = cast<Instruction>(U.getUser());
        if (!isa<PHINode>(UserInst)) {
            BasicBlock *UserBB = UserInst->getParent();

            // The original users in the OrigHeader are already using the
            // original definitions.
            if (UserBB == OrigHeader)
            continue;

            // Users in the OrigPreHeader need to use the value to which the
            // original definitions are mapped.
            if (UserBB == OrigPreheader) {
            U = OrigPreHeaderVal;
            continue;
            }
        }

        // Anything else can be handled by SSAUpdater.
        SSA.RewriteUse(U);
        }
    }
    }""")
    print(tokenizer.full_tokenize())
    print(tokenizer.full_tokenize_compressed())