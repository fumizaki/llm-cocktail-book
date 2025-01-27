"use client";

import { cn } from "@/lib/style";
import { useRouter } from "next/navigation";
import { useActionState, useEffect } from "react";
import { useToast } from "@/hooks/use-toast";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
	Card,
	CardHeader,
	CardTitle,
	CardDescription,
	CardContent,
} from "@/components/ui/card";
import { createAction } from "@/server-actions/chatbot/create";

type Props = {
	className?: string;
};

export const CreateChatbotForm = ({ className }: Props) => {
	const router = useRouter();
	const { toast } = useToast();

	const [state, formAction, isPending] = useActionState(createAction, {
		inputs: {
			title: "",
		},
	});

	useEffect(() => {
		if (state.success) {
			toast({
				title: "Success",
				description: "Create Chatbot Successfully",
			});
			router.push("/chatbot");
		} else if (state.success === false) {
			toast({
				variant: "destructive",
				title: "Error",
				description: "Error while Creating Chatbot",
			});
		}
	}, [state]);

	return (
		<form
			action={formAction}
			className={cn(
				`w-full flex flex-col justify-center items-center`,
				className,
			)}
		>
			<Card className={`w-full`}>
				<CardHeader>
					<CardTitle>Create Chatbot</CardTitle>
					<CardDescription>Chat with LLM</CardDescription>
				</CardHeader>
				<CardContent className="flex flex-col gap-3">
					<Label className={'flex flex-col gap-1.5'}>
						Title
						<Input
							type={"text"}
							name={"inputs.title"}
							defaultValue={state.inputs?.title}
							className={state.validationErrors?.title && "bg-red-200"}
						/>
						{state.validationErrors?.title && (
							<small>{state.validationErrors?.title}</small>
						)}
					</Label>
					<Button type="submit" disabled={isPending}>
						Create Chatbot
					</Button>
				</CardContent>
			</Card>
		</form>
	);
};
