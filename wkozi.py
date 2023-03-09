import numpy as np, random, time
# This is the main function to design the random path
def randomwalk3D(n,a,b,c,past,x1,x2,y1,y2,z1,z2):
    # Initialize parameters
    start=time.time()
    directions = ["UP", "DOWN", "LEFT", "RIGHT", "IN", "OUT"]
    previousStep= random.choice(directions)
    print(n,a,b,c)
    path = np.zeros((n,3))
    pathPast  = np.concatenate((path,past))
    # l is used to check if a new position already exists in the path
    l = len(pathPast)

    # Create an array positions, to choose the beginning of the chromosome
    xyz = np.zeros((1,3))
    xyzN = np.zeros((1,3))
    for k1 in range(x1,x2):
        for k2 in range(y1,y2):
            for k3 in range(z1,z2):
                if pow(k1/a,2)+pow(k2/b,2)+pow(k3/c,2) < 1:
                    xyzN[0,:] = [k1,k2,k3]
                    xyz = np.concatenate((xyz,xyzN))
    #print(xyz)
    xyz = np.delete(xyz, 0, axis=0)
    np.random.shuffle(xyz)
    choise = xyz[0,:]
    path[0,:] = choise
    print(path[0,:])

    # Check if the starting point of the chromosome, already exists in the path, to avoid overlaps
    j = 0
    start=time.time()
    while j < 10:
        dt = time.time()-start
        if np.any(np.all(pathPast == path[0,:], axis=1)):
        #if (np.array_equal(path[0,:],pathPast[j,:])):
            j = 0
        if dt>4:
            np.random.shuffle(xyz)
            path[0,:] = xyz[0,:]
            start=time.time()
        j += 1

    # Create the random walk
    start=time.time()
    i=1
    while i < n:
        # Check if the code is stuck in the same position for a lot of time.
        # If yes return some positions back and try again.
        dt = time.time()-start
        if dt>3:
            if i>10:
                i -= 10
                start=time.time()
                print("stopped: ", i)
            else:
                i -=1
                start=time.time()
        #print(i)
        newPos = np.zeros((1,3))

        # Choose a random step from the available directions
        step = random.choice(directions)
        # Avoid straight paths. If tries to avoid straight, but they can still exist.
        # Using while, straights will not exist. May lead to not be able to design the DNA.!
        if step==previousStep:
        #while step==previousStep:
            #print("-->")
            random.shuffle(directions)
            step = random.choice(directions)
        #print(step)
        previousStep = step

        # After a direction is chosen, the step is used to produce the new position.
        # The same steps are used in every step, so only for the "RIGHT", comments have been written.
        if step == "RIGHT":
            newX = path[i-1,0] + 1
            # Geometrical limitations. New position should be in the ellipsoid.
            d = pow(newX/a,2)+pow(path[i-1,1]/b,2)+pow(path[i-1,2]/c,2)
            if ((d > 1) or (newX>x2) or (newX<=x1)):
                continue
            # New position should not belong to the already developed path.
            else:
                newPos=np.array([ newX, path[i-1,1], path[i-1,2] ])
                if np.any(np.all(pathPast == newPos, axis=1)):
                    continue
                else:
                    path[i,:] = np.array([ path[i - 1,0] +1, path[i - 1,1], path[i - 1,2] ])
                    i += 1
                    start=time.time()

        elif step == "LEFT":
            newX = path[i-1,0] - 1
            d = pow(newX/a,2)+pow(path[i-1,1]/b,2)+pow(path[i-1,2]/c,2)
            if ((d > 1) or (newX>x2) or (newX<=x1)):
                continue
            else:
                newPos=np.array([ newX, path[i-1,1], path[i-1,2] ])
                if np.any(np.all(pathPast == newPos, axis=1)):
                    continue
                else:
                    path[i,:] = np.array([ path[i - 1,0] -1, path[i - 1,1], path[i - 1,2] ])
                    i += 1
                    start=time.time()

        elif step == "UP":
            newY = path[i-1,1] + 1
            d = pow(path[i-1,0]/a,2)+pow(newY/b,2)+pow(path[i-1,2]/c,2)
            if ((d > 1) or (newY>y2) or (newY<=y1)):
                continue
            else:
                newPos=np.array([ path[i-1,0], newY, path[i-1,2] ])
                if np.any(np.all(pathPast == newPos, axis=1)):
                    continue
                else:
                    path[i,:] = np.array([ path[i - 1,0], path[i - 1,1] +1, path[i - 1,2] ])
                    i += 1
                    start=time.time()

        elif step == "DOWN":
            newY = path[i-1,1] - 1
            d = pow(path[i-1,0]/a,2)+pow(newY/b,2)+pow(path[i-1,2]/c,2)
            if ((d > 1) or (newY>y2) or (newY<=y1)):
                continue
            else:
                newPos=np.array([ path[i-1,0], newY, path[i-1,2] ])
                if np.any(np.all(pathPast == newPos, axis=1)):
                    continue
                else:
                    path[i,:] = np.array([ path[i - 1,0], path[i - 1,1] -1, path[i - 1,2] ])
                    i += 1
                    start=time.time()

        elif step == "IN":
            newZ = path[i-1,2] - 1
            d = pow(path[i-1,0]/a,2)+pow(path[i-1,1]/b,2)+pow(newZ/c,2)
            if ((d > 1) or (newZ>z2) or (newZ<=z1)):
                continue
            else:
                newPos=np.array([ path[i-1,0], path[i-1,1], newZ ])
                if np.any(np.all(pathPast == newPos, axis=1)):
                    continue
                else:
                    path[i,:] = np.array([ path[i - 1,0], path[i - 1,1], path[i - 1,2] -1 ])
                    i += 1
                    start=time.time()

        elif step == "OUT":
            newZ = path[i-1,2] + 1
            d = pow(path[i-1,0]/a,2)+pow(path[i-1,1]/b,2)+pow(newZ/c,2)
            if ((d > 1) or (newZ>z2) or (newZ<=z1)):
                continue
            else:
                newPos=np.array([ path[i-1,0], path[i-1,1], newZ ])
                if np.any(np.all(pathPast == newPos, axis=1)):
                    continue
                # Left this next part for historical reasons
                #for j in range(l):
                #    if (np.array_equal(newPos,pathPast[j,:])):
                #        kozi = True
                #if (kozi==True):
                #    continue
                else:
                    path[i,:] = np.array([ path[i - 1,0], path[i - 1,1], path[i - 1,2] +1 ])
                    #path[i,0] = path[i - 1,0]
                    #path[i,1] = path[i - 1,1]
                    #path[i,2] = path[i - 1,2] + 1
                    i += 1
                    start=time.time()

        pathPast[i,:] = path[i-1,:]
    return path
